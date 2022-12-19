# ブロブの検出

import cv2
import copy

img = cv2.imread("src/Blob.png")
img_g = cv2.imread("src/Blob.png", 0)

ret, img_bi = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY)

nLabels, labelImage, stats, centroids = cv2.connectedComponentsWithStats(img_bi)
# nLabels:ブロブの数(黒も一つとしてカウント)
# labelImage:ブロブのID
# stats:[xmin, ymin, w, h, 面積(ピクセルをカウント)]
# centroids:重心座標

img_blob = copy.deepcopy(img)
h, w = img_g.shape
color = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]]

for y in range(h):
    for x in range(w):
        if labelImage[y, x] > 0:
            img_blob[y, x] = color[labelImage[y, x] - 1]

for i in range(1, nLabels):  # 0番目は背景の黒なので
    xc = int(centroids[i][0])
    yc = int(centroids[i][1])
    font = cv2.FONT_HERSHEY_COMPLEX
    scale = 1
    color = (255, 255, 255)
    cv2.putText(img_blob, str(stats[i][-1]), (xc, yc), font, scale, color)

cv2.imshow("img", img_blob)
cv2.waitKey(0)
cv2.destroyAllWindows()
