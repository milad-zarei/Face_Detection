Face Detection App with Start/Stop Control
This project is a simple real-time face detection application using OpenCV and Tkinter, allowing the user to start and stop face detection via buttons.

Features
Uses webcam for real-time face detection

Displays the total number of detected faces in each frame

Provides GUI buttons to start and stop detection

Draws green rectangles around detected faces with face numbering

Requirements
Python 3.x

OpenCV (opencv-python)

Tkinter (usually included by default with Python)

Installation
Make sure Python is installed, then install OpenCV via pip:

bash
Copy
Edit
pip install opencv-python
Usage
Run the face_detection_app.py script.

Click the Start button to open the webcam and begin face detection.

Click the Stop button to stop detection and release the webcam.

Alternatively, press the q key to close the display window and stop detection.

Code Explanation
Uses cv2.CascadeClassifier with the Haarcascade model for face detection.

Organized in a class FaceDetectionApp which manages the GUI and detection logic.

Face detection runs in a separate thread to keep the GUI responsive.

Troubleshooting
If the webcam fails to open, an error message will appear.

Make sure the program has permission to access the webcam.

Possible Improvements
Add functionality to save detected face images

Use more advanced face detection models