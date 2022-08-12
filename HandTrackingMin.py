import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture (0, cv2.CAP_DSHOW)

mpH = mp.solutions.hands
hands = mpH.Hands ()
mpD = mp.solutions.drawing_utils

pT = 0
cT = 0

while (capture.isOpened ()):
    ret, frame = capture.read ()
    imgRGB = cv2.cvtColor (frame, cv2.COLOR_BGR2RGB)
    results = hands.process (imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate (handLms.landmark):
                # print(id,lm)
                h, w, c = frame.shape
                cx, cy = int (lm.x * w), int (lm.y * h)
                print (id, cx, cy)

                """
                MARCA PUNTA DE DEDOS

                if id == 4:
                    cv2.circle(frame, (cx,cy), 10, (0, 255, 0), cv2.FILLED)
                if id == 8:
                    cv2.circle(frame, (cx,cy), 10, (0, 255, 0), cv2.FILLED)
                if id == 12:
                    cv2.circle(frame, (cx,cy), 10, (0, 255, 0), cv2.FILLED)
                if id == 16:
                    cv2.circle(frame, (cx,cy), 10, (0, 255, 0), cv2.FILLED)
                if id == 20:
                    cv2.circle(frame, (cx,cy), 10, (0, 255, 0), cv2.FILLED)
                """

            mpD.draw_landmarks (frame, handLms, mpH.HAND_CONNECTIONS)

    cT = time.time ()
    fps = 1 / (cT - pT)
    pT = cT

    cv2.putText (frame, str (int (fps)), (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    cv2.imshow ('webCam', frame)

    if (cv2.waitKey (1) == ord ('s')):
        break
capture.release ()
cv2.destroyAllWindows ()