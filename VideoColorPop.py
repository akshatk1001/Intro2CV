import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Nothing is found. Error")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blue_lower = np.array([110, 150, 20])
    blue_upper = np.array([130, 255, 255])
    
    mask = cv2.inRange(hsv, blue_lower, blue_upper)
    not_mask = cv2.bitwise_not(mask)
    
    blue = cv2.bitwise_and(frame, frame, mask = mask)
    bw = cv2.bitwise_and(gray, gray, mask = not_mask)
    bw = np.stack((bw,)*3, axis = -1)

    final = cv2.add(blue, bw)
    cv2.imshow("Frame", final)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

