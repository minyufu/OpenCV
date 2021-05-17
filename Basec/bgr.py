import numpy as np
import cv2
#建立512x512 的黑色畫布
gc = np.zeros((512, 512, 3), np.uint8)
#用(B, G, R) = (255, 255, 255): 白色填滿畫布
gc.fill(255)
# 從(10, 50) 到(400, 300) 畫條藍色且寬度為5的直線
#cv2.line(gc, (10, 50), (400, 300), (255, 0, 0), 5)

# 矩形
# cv2.rectangle(gc, (30, 50), (200, 280), (0, 255, 0), 3)

# 圓形
# cv2.circle(gc, (200, 300), 100, (0, 0, 255), -1)

# 橢圓
# cv2.ellipse(gc, (256, 256), (100, 50), 0, 90, 270, (255, 0, 0), 3)

# 多邊形
# pts = np.array(((10,5), (100,100), (170,120), (200,50)))
# cv2.polylines(gc, [pts], True, (0, 0, 0), 2)

# 顯示文字
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(gc, 'OpenCV', (10,200), font, 4, (0,0,0), 2, cv2.LINE_AA)

cv2.imshow("draw", gc)
cv2.waitKey(0)
cv2.destroyAllWindows()