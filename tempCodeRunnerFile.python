import cv2

image=cv2.imread('dog.1.jpg')
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('Dog', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Dog', 800,500)


cv2.imshow('Dog', grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Processed Image DImensions: {grey_image}")
