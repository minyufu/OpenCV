import cv2
#IMREAD_COLOR: 1
#IMREAD_GRAYSCALE: 0
#IMREAD_UNCHANGED: -1
frame = cv2.imread('my.jpg', 1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()