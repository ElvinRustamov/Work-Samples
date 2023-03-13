import HandTrackingModule as htm
import cv2
import mediapipe as mp
import time

pTime = 0
cTime = 0

# For webcam
cap = cv2.VideoCapture(0)

detector = htm.handDetector()

while True:
    success, img = cap.read()
    # Convert img to RGB because hands object work with RGB
    img = detector.find_hands(img)
    position = detector.find_position(img)
    if len(position) != 0:
        print(position)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    cv2.imshow('Image', img)
    cv2.waitKey(1)
