# アファイン変換

import cv2
import numpy as np

img = cv2.imread("src/grapes.jpg")
h, w = img.shape[:2]
dx, dy = 50, 60

afn_mat = np.float32([[1, 0, dx], [0, 1, dy]])  # アファイン変換の変換行列の定義
img_afn = cv2.warpAffine(img, afn_mat, (w, h))

cv2.imshow("trans", img_afn)
cv2.waitKey(0)
cv2.destroyAllWindows()

rot_mat = cv2.getRotationMatrix2D((w/2, h/2), 40, 1)
img_afn2 = cv2.warpAffine(img, rot_mat, (w, h))

cv2.imshow("rotation", img_afn2)
cv2.waitKey(0)
cv2.destroyAllWindows()
