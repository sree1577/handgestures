# Hand Gesture Recognition

This project uses OpenCV and MediaPipe to recognize hand gestures in real-time using your webcam. It detects and classifies the following gestures:

- Fist
- Palm
- Thumb Up
- Thumb Down
- Index Finger Up

## Features
- Real-time hand tracking and gesture recognition
- Visualizes hand landmarks and gesture name on the video feed

## Requirements
- Python 3.11 or higher
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)

## Installation
1. Clone or download this repository.
2. Install the required packages:
   ```sh
   pip install opencv-python mediapipe
   ```

## Usage
Run the script using Python:
```sh
python handgestures.py
```
A window will open showing the webcam feed with detected hand landmarks and the recognized gesture name.

## Example
![Hand Gesture Recognition Example](assets\image\Screenshot 2025-08-06 214407.png)

## Notes
- Press `Esc` to exit the application.
- Make sure your webcam is connected and accessible.

## License
This project is for educational purposes.
