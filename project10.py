# 特徴抽出

import cv2
import numpy as np
import copy

img = cv2.imread("src/buildings.jpg")
img_g = cv2.imread("src/buildings.jpg", 0)

img_harris = copy.deepcopy(img)
img_dst = cv2.cornerHarris(img_g, 2, 3, 0.04)
img_harris[img_dst > 0.05 * img_dst.max()] = [0, 0, 255]

cv2.imshow("img_harris", img_harris)

img_kaze = copy.deepcopy(img)
kaze = cv2.KAZE_create()
kp1 = kaze.detect(img, None)
img_kaze = cv2.drawKeypoints(img_kaze, kp1, None)

cv2.imshow("img_kaze", img_kaze)

img_akaze = copy.deepcopy(img)
akaze = cv2.AKAZE_create()
kp2 = akaze.detect(img, None)
img_akaze = cv2.drawKeypoints(img_akaze, kp2, None)

cv2.imshow("img_akaze", img_akaze)

img_orb = copy.deepcopy(img)
orb = cv2.ORB_create()
kp3 = orb.detect(img_orb)
img_orb = cv2.drawKeypoints(img_orb, kp3, None)

cv2.imshow("img_orb", img_orb)

cv2.waitKey(0)
cv2.destroyAllWindows()
