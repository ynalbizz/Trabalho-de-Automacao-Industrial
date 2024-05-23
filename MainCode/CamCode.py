from cvzone.HandTrackingModule import HandDetector
import cv2
from Areas import areasList

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, modelComplexity=1, detectionCon=0.8)
# Continuously get frames from the webcam
def _GetHandsInfo():
    while True:
        # Capture each frame from the webcam
        # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
        success, img = cap.read()

        # Find hands in the current frame
        # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
        # The 'flipType' parameter flips the image, making it easier for some detections
        hands, img = detector.findHands(img, draw=True, flipType=True)

        for area in areasList:
                colorr = (255, 0, 255)
                cv2.rectangle(img, areasList[area].infos("origin"), areasList[area].infos("end"), colorr, 2)

        # Check if any hands were detected
        for hand in hands:

            lmList1 = hand["lmList"]  # List of 21 landmarks for the first hand
            # calculate distance between two fingers of hand 1
            length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[4][0:2], img, color=(255, 0, 255), scale=10)
            #add new values on Hand
            hand["fingers"] = detector.fingersUp(hand)
            hand["length"] = length

        #inicializate Lengthbetween Var
        lengthbetween = None

        # Check if a second hand was detected
        if len(hands) == 2:
            # Calculate distance between the index fingers of both hands and draw it on the image
            lengthbetween, info, img = detector.findDistance(hands[0]["lmList"][8][0:2], hands[1]["lmList"][8][0:2], img, color=(255, 0, 0), scale=10)

        # Display the image in a window
        cv2.imshow("Camera", img)

        # Keep the window open and update it for each frame; wait for 1 millisecond between frames
        cv2.waitKey(1)
        yield (hands, lengthbetween)

