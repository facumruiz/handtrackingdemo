# ERROR1 (create_int(): incompatible function arguments)
# https://stackoverflow.com/questions/69686420/typeerror-create-int-incompatible-function-arguments


import cv2
import mediapipe as mp
import time


class handDetector ():
    def __init__ (self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands (self.mode, self.maxHands, self.modelComplex,
                                         self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands (self, frame, draw=True):
        imgRGB = cv2.cvtColor (frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process (imgRGB)
        # print(results.multi_hand_landmarks)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks (frame, handLms, self.mpHands.HAND_CONNECTIONS)
        return frame

        # for id, lm in enumerate (handLms.landmark):
        # print(id,lm)
        # h, w, c = frame.shape
        # cx, cy = int (lm.x * w), int (lm.y * h)
        # print (id, cx, cy)


def main ():
    pT = 0
    cT = 0
    capture = cv2.VideoCapture (0, cv2.CAP_DSHOW)
    detector = handDetector ()

    while (capture.isOpened ()):
        ret, frame = capture.read ()
        frame = detector.findHands (frame)

        cT = time.time ()
        fps = 1 / (cT - pT)
        pT = cT

        cv2.putText (frame, str (int (fps)), (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

        cv2.imshow ('webCam', frame)

        if (cv2.waitKey (1) == ord ('s')):
            break
    capture.release ()
    cv2.destroyAllWindows ()


if __name__ == "__main__":
    main ()
