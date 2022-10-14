# Face-Eye-Detection

OpenCV is an open-source computer vision library that uses machine learning algorithms for face detection, object tracking or colours detection.

Approach:
Capture the video from the webcam.
Convert the frames to grayscale since the cascade algorithm works only with greyscale.
Detect the faces using multi-scale. It takes III arguments — the input image, scaleFactor and minNeighbors. Scale Factor specifies how much the image size is reduced at each image scale and min neighbours specify how many neighbours each candidate rectangle should have to retain it.
Draw the blue rectangle on the faces.
Draw the green rectangle on the eyes.
