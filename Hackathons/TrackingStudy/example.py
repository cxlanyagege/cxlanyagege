"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
# encoding:utf-8
import time
import cv2 as cv
import numpy as np
from gaze_tracking import GazeTracking
from gaze_tracking.utils import addText

gaze = GazeTracking()
webcam = cv.VideoCapture(0)

lu,ld,ru,rd = 0,0,0,0

while True:
    img = np.zeros((1000, 1900, 3), np.uint8)
    text = u"哪里不懂看哪里"
    img = addText(img, 750, 10, text, 40, (147, 58, 31), 2)
    org = (40, 80)
    fontFace = cv.FONT_HERSHEY_COMPLEX
    fontScale = 1
    fontcolor = (0, 255, 0)  # BGR
    thickness = 1
    lineType = 4
    bottomLeftOrigin = 1

    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    example1 = ""
    example2 = ""
    example3 = ""

    # trans = ""
    if gaze.is_left():
        lu += 1
        ld, ru, rd = 0, 0, 0
        if lu > 15 and lu < 30:
            example1 = "苹果"
            img = addText(img, 110, 220, example1, 40, (147, 58, 31), 2)
    if gaze.is_center():
        ld += 1
        lu, ru, rd = 0, 0, 0
        if ld > 15 and ld < 30:
            example2 = "香蕉"
            img = addText(img, 890, 220, example2, 40, (147, 58, 31), 2)
    if gaze.is_right():
        ru += 1
        ld, lu, rd = 0, 0, 0
        if ru > 15 and ru < 30:
            example3 = "杨梅"
            img = addText(img, 1800, 220, example3, 40, (147, 58, 31), 2)

    cv.putText(frame, text, (90, 60), cv.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    hr = gaze.horizontal_ratio()
    vr = gaze.vertical_ratio()
    cv.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv.putText(frame, "Horizontal ratio: " + str(hr), (90, 200), cv.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv.putText(frame, "Vertical ratio: " + str(vr), (90, 235), cv.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv.putText(frame, "Direction " + gaze.getDirection(), (90, 300), cv.FONT_HERSHEY_DUPLEX, 0.9,
                (147, 58, 31), 1)
    cv.putText(img, "apple", (90, 220), cv.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv.putText(img, "banana", (890, 220), cv.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv.putText(img, "arbutus", (1790, 220), cv.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv.imshow("Debug Window Demo", frame)
    cv.imshow("Eyellower Demo", img)

    if cv.waitKey(1) == 27:
        break
