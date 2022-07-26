import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

cap = cv2.VideoCapture(0)

k = 0

while True:
    ret, frame = cap.read()

    # Identify if 'ESC' is pressed or not
    if (k == 27):
        break

    # Identify if 'e' or 'E' is pressed
    if (k == 101 or k == 69):
        cv2.putText(frame, "E is pressed, press Z or ESC", (100, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3);

    # Identify if 'z' or 'Z' is pressed
    if (k == 90 or k == 122):
        cv2.putText(frame, "Z is pressed", (100, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        cv2.imshow("Image", frame)

        # Increase waitkey to show display properly
        k = cv2.waitKey(10000) & 0xFF

cap.release()
cv2.destroyAllWindows()
