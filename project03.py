# 畳み込みの基礎

import cv2
import numpy as np

kernel = np.ones((3, 3)) / 9
img = cv2.imread("src/Lena.jpg", 0)

img_ke1 = cv2.filter2D(img, -1, kernel)  # 畳み込み

cv2.imshow("img", img_ke1)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel2 = np.zeros((3, 3))
kernel2[0, 0] = 1
kernel2[1, 0] = 2
kernel2[2, 0] = 1
kernel2[0, 2] = -1
kernel2[1, 2] = -2
kernel2[2, 2] = -1
# kernel2[0, 0] = 1/6
# kernel2[1, 0] = 1/6
# kernel2[2, 0] = 1/6
# kernel2[0, 2] = 1/6
# kernel2[1, 2] = 1/6
# kernel2[2, 2] = 1/6

img_ke2 = cv2.filter2D(img, -1, kernel2)

cv2.imshow("img", img_ke2)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
