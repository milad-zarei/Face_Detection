import cv2
import threading
import tkinter as tk
from tkinter import messagebox

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

class FaceDetectionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("تشخیص چهره با کنترل Start/Stop")

        #  دکمه‌ها
        self.start_button = tk.Button(window, text="شروع", command=self.start_detection)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(window, text="توقف", command=self.stop_detection, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.cap = None
        self.running = False

    def start_detection(self):
        if self.running:
            return
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("خطا", "وبکم باز نشد!")
            return
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.detect_faces).start()

    def detect_faces(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            for i, (x, y, w, h) in enumerate(faces):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f'Face {i+1}', (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.putText(frame, f'Total Faces: {len(faces)}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Face Detection", frame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                self.stop_detection()
                break 

        self.cap.release()
        cv2.destroyAllWindows()
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def stop_detection(self):
        if self.running:
            self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectionApp(root)
    root.mainloop()