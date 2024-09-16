from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np


def addText(frame,x,y,text, size, color, wid):
    img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    imgD = ImageDraw.Draw(img)
    font = ImageFont.truetype("gaze_tracking/SourceHanSerifSC-Regular.otf", size, encoding="utf-8")
    imgD.text((x, y), text, color, font=font)
    return cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
