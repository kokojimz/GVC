import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # Changed camera index to 0
detector = htm.handDetector()

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Failed to grab frame from camera. Check camera index and connection.")
        break

    img = detector.findHands(img, draw=True)
    lmList, _ = detector.findPosition(img, draw=False)  # Ensure findPosition returns a tuple (lmList, bbox)
    
    if lmList and len(lmList) > 4:
        print(lmList[4])  # Check if there are enough landmarks before accessing

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
