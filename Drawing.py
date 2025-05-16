import cv2
import numpy as np

def nothing(x):
    pass

img=np.zeros((300,512,3), np.uint8)
cv2.namedWindow('Canvas')

cv2.createTrackbar('R', 'Canvas', 0,255, nothing)
cv2.createTrackbar('G', 'Canvas', 0,255, nothing)
cv2.createTrackbar('B', 'Canvas', 0,255, nothing)
cv2.createTrackbar('Thickness', 'Canvas', 1,10, nothing)

drawing=False
ix,iy=-1,-1

def draw(event, x,y,flags,param):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            r=cv2.getTrackbarPos('R', 'Canvas')
            g=cv2.getTrackbarPos('G', 'Canvas')
            b=cv2.getTrackbarPos('B', 'Canvas')
            thickness=cv2.getTrackbarPos('Thickness', 'Canvas')
            cv2.line(img, (ix,iy), (x,y), (b,g,r), thickness)
            ix,iy = x, y
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.setMouseCallback('Canvas', draw)

while True:
    cv2.imshow('Canvas', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 