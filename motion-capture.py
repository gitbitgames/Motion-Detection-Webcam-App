import cv2, time
from datetime import datetime as dt

first_frame = None
### Status list will be used for recording motion events
status_list = [0,0]
times = []

### Instructing the program to initiate camera and wait 1 second (Some people's cameras can take a moment to initialize)
video = cv2.VideoCapture(0)
video.read()
time.sleep(1)

while True:
    ### Read from the video camera
    check, frame = video.read()
    status = 0

    ### Convert to grayscale and add a blur effect
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    ### Get the delta frame
    if first_frame is None:
        first_frame = gray
        continue

    ### Convert delta frame to grayscale and apply a threshold
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    ### Find contours of moving objects in frame
    ( cnts, _ ) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ### We only want contours with a shape that is larger than 1000px
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        ### Otherwise, we want to highlight it with a rectangle in the current frame
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            3
            )

    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(dt.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(dt.now())

    
    ### Show delta frame
    cv2.imshow("Delta Frame", delta_frame)
    ### Show threshold frame
    cv2.imshow("Threshold Frame", thresh_frame)
    ### Show color frame with rectangles indicating movement
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key==ord('q'):
        break

    print(status_list)

video.release()
cv2.destroyAllWindows