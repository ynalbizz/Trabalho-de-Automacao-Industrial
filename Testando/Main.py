import GesturesLibrary as GestLib
from cvzone.HandTrackingModule import HandDetector
import cv2
import AuxiliarLibrary as Aux

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, modelComplexity=1, detectionCon=0.8)

# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()

    if not success:
        continue

    area = [
        # lista de Areas
        Aux.Area((300, 300), 50, 50, img, lambda: print("ag1")),
        Aux.Area((150, 150), 100, 100, img, lambda: print("ag2"))
    ]

    area[1].drawArea()
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    for hand in hands:
        # Information for the first hand detected
        lmList1 = hand["lmList"]  # List of 21 landmarks for the first hand
        bbox1 = hand["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand['center']  # Center coordinates of the first hand
        handType1 = hand["type"]  # Type of the first hand ("Left" or "Right")
        fingers1 = detector.fingersUp(hand)

        # calculate distance between two fingers of hand 1
        length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[4][0:2], img, color=(255, 0, 255), scale=10)
       
        GestLib.onehandcontroller(handType1, fingers1, length, center1, area)

    # Check if a second hand is detected
    if len(hands) == 2:
        # Calculate distance between the index fingers of both hands and draw it on the image
        lengthbetween, info, img = detector.findDistance(hands[0]["lmList"][8][0:2], hands[1]["lmList"][8][0:2], img, color=(255, 0, 0), scale=10)
        GestLib.twohandcontroller(lengthbetween)

        print(" ")  # New line for better readability of the printed output

    # Display the image in a window
    cv2.imshow("Image", img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)
