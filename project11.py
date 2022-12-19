# 顔検出

import cv2

HAAR_FILE = "C:/Users/masac/Anaconda3/pkgs/libopencv-3.4.2-h20b85fd_0/Library/etc/haarcascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

img = cv2.imread("src/Solvay_conference_1927.jpg")
img_g = cv2.imread("src/Solvay_conference_1927.jpg", 0)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

height, width = img_g.shape[0:2]
cv2.rectangle(img_g, (0, 0), (width, int(height / 3)), (0, 0, 0), -1)

face = cascade.detectMultiScale(img_g, minSize=(50, 50))
print(face)
# face[x, y, w, h]

for x, y, w, h in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("face.jpg", img)
