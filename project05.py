# エッジの検出(Sobel, Laplacian)

import cv2

img = cv2.imread("src/Lena.jpg", 0)

img_sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
img_sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

img_sobelx = cv2.convertScaleAbs(img_sobelx)
img_sobely = cv2.convertScaleAbs(img_sobely)

cv2.imshow("X", img_sobelx)
cv2.imshow("Y", img_sobely)
cv2.waitKey()
cv2.destroyAllWindows()

img_lap = cv2.Laplacian(img, cv2.CV_32F)
# Laplacianは2次の微分なので値が小さくエッジが弱い
img_lap = cv2.convertScaleAbs(img_lap)
# 2倍にするとノイズがのってしまう
img_lap2 = img_lap * 2

cv2.imshow("lap", img_lap)
cv2.imshow("lap2", img_lap2)
cv2.waitKey()
cv2.destroyAllWindows()

# ノイズを避けるために平滑化を行ってからラプラシアンを使う
img_blur = cv2.GaussianBlur(img, (3, 3), 2)
img_lapG = cv2.Laplacian(img_blur, cv2.CV_32F)
img_lapG = cv2.convertScaleAbs(img_lapG)
img_lapG *= 2

cv2.imshow("lapG", img_lapG)
cv2.imshow("lap2", img_lap2)
cv2.waitKey()
cv2.destroyAllWindows()
