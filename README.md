# GVC (Gesture Volume Control)

## Overview
GVC (Gesture Volume Control) is a Python-based application that allows users to control the volume of their computer using hand gestures. 
This project utilizes OpenCV for real-time video capture and MediaPipe for hand tracking. The system volume is adjusted in real-time based on the position and movement of the user's hand as captured by the webcam.



https://github.com/kokojimz/GVC/assets/93468154/e52a1b34-7c1f-46e6-980d-1cbe796a2150


## Features
<ul>
  <li>Real-Time Hand Tracking: Uses MediaPipe to accurately track hand movements in real-time.</li>
  <li>Volume Control: Adjusts the system's volume level based on the distance between the thumb and index finger.</li>
  <li>Visual Feedback: Provides a visual representation of the current volume level and hand landmarks.</li>
</ul>

## Installation
```bash
pip install opencv-python
pip install mediapipe
pip install numpy
pip install pycaw
pip install comtypes
```

## Usage
To use GVC, clone the repository and run the main script:
```bash
git clone https://github.com/kokojimz/GVC.git
cd GVC
python VolumeControl.py
```
Position your hand within the camera's view and adjust the volume by bringing your thumb and index finger closer or further apart.

## How It Works?
GVC captures video frames from the webcam and processes them using OpenCV. MediaPipe's hand tracking solution is used to detect and track the position of the hand in real-time. 
The distance between the thumb and index finger is calculated and mapped to the system's volume range using pycaw.

