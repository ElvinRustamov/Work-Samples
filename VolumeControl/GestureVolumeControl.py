import cv2
import time
import numpy as np
import HandTrackingModule as hpm
import math

width_camera, height_camera = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, width_camera)
cap.set(4, height_camera)
previous_time = 0

detector = hpm.handDetector(detectionCon = 0.7)


from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPercentage = 0


while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    landmark_list = detector.find_position(img, draw=False)
    if len(landmark_list) != 0:

        x1, y1 = landmark_list[4][1], landmark_list[4][2]
        x2, y2 = landmark_list[8][1], landmark_list[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (255, 255, 200), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 255, 200), cv2.FILLED)

        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 200), 3)
        cv2.circle(img, (cx, cy), 10, (255, 255, 200), cv2.FILLED)


        length = math.hypot(x2 - x1, y2 - y1)
        vol = np.interp(length, [50, 250], [minVol, maxVol])
        volBar = np.interp(length, [50, 250], [400, 150])
        volPercentage = np.interp(length, [50, 250], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f': {int(volPercentage)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
    current_time = time.time()

    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

    cv2.imshow('Img', img)
    cv2.waitKey(1)