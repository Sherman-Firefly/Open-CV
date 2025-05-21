import cv2

import numpy as np


img = np.zeros((512, 512, 3), np.uint8)


def mouse_drawing_event(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        cv2.circle(img, (x, y), 20, (150, 255, 0), -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        pt2_x = x + 20
        pt2_y = y + 20
        cv2.rectangle(img, (x, y), (pt2_x, pt2_y), (200, 215, 150), 10)
      


cv2.namedWindow('Canvas')

cv2.setMouseCallback('Canvas', mouse_drawing_event)


while True:

    cv2.imshow('Canvas', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()