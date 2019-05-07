import numpy as np, cv2 as cv, os

image = cv.imread('face.jpg')
grayValue = image[:,:,0] * 2.28
gray_img = grayValue.astype(np.uint8)

cv.imshow("Original", image)
cv.imshow("GrayScale", gray_img)
cv.waitKey(0)
cv.destroyAllWindows()