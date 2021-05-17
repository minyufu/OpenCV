import cv2
# ASCII 代碼
ESC = 27

# 啟動攝影機
cap = cv2.VideoCapture(0)
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
ratio = cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) / cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
WIDTH = 400
HEIGHT = int(WIDTH / ratio)

# 取得影像
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ESC:
        cv2.destroyAllWindows()
        break