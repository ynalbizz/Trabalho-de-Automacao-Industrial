import definindo_gestos as gestoslib
from cvzone.HandTrackingModule import HandDetector
import cv2

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

    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")
        fingers1 = detector.fingersUp(hand1)
        length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[4][0:2], img, color=(255, 0, 255),scale=10)#calculate distance between two fingers of hand 1
        gestoslib.OneHandcontroller(handType1,fingers1,length)


        # Check if a second hand is detected
        if len(hands) == 2:
            # Information for the second hand
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]
            fingers2 = detector.fingersUp(hand2)
            length, info, img = detector.findDistance(lmList2[8][0:2], lmList2[4][0:2], img, color=(255, 0, 255),scale=10)#calculate distance between two fingers of hand 2
            
            # Calculate distance between the index fingers of both hands and draw it on the image
            lengthbetween, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img, color=(255, 0, 0),scale=10)

            gestoslib.TwoHandcontroller(handType2,fingers2,length,lengthbetween)


        print(" ")  # New line for better readability of the printed output

    # Display the image in a window
    cv2.imshow("Image", img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)