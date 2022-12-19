# エッジの検出(Canny)

import cv2

img = cv2.imread("src/Lena.jpg")

img_canny = cv2.Canny(img, 100, 200)
img_canny2 = cv2.Canny(img, 200, 200)
cv2.imshow("Canny", img_canny)
cv2.imshow("Canny2", img_canny2)
cv2.waitKey(0)
cv2.destroyAllWindows()
