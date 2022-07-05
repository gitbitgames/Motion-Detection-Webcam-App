This is an application for motion detection. It captures a single still image upon initialization, and then compares new images against that one. If it detects movement, you should be able to see the movement being tracked on both the "Color" and "Threshold" images.

In order to run the program:
1. Download motion-capture.py
2. Download module cv2@4.6.0
3. Run the file in Python 3.9.12
4. Give permission to the program to access your camera if it pops up.
5. Make sure that you are out of frame when starting the program so that it can take a clean picture upon intitialization.

You should see 3 different camera styles suited to movement tracking - grayscale, black & white, and color

There is also a feature to record any significant camera-movement events in a log for review.