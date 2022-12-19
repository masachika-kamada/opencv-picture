# 画像の平滑化

import cv2

img = cv2.imread("src/buildings.jpg")

# 単純な平滑化
img_blur = cv2.blur(img, (3, 3))
cv2.imshow("img", img_blur)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 第3引数のシグマの調整によって平滑化の度合いを調整できる
img_ga = cv2.GaussianBlur(img, (9, 9), 2)
cv2.imshow("img", img_blur)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# カーネルの中央値によって塗りつぶしを決定
img_me = cv2.medianBlur(img, 5)
cv2.imshow("img", img_blur)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# エッジを保存して平滑化
img_bi = cv2.bilateralFilter(img, 20, 30, 30)
cv2.imshow("img", img_blur)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
