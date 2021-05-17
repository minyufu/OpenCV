import cv2, time
cap = cv2.VideoCapture(0)
# 這三秒鐘是讓攝影機有時間調整曝光、白平衡與對焦
time.sleep(3)
ret, frame = cap.read()
frame = cv2.flip(frame, 1)
cv2.imwrite("my2.jpg", frame)