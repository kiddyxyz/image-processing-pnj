import numpy as np, cv2 as cv, os

image = cv.imread('face.jpg')
grayValue = 0.07 * image[:,:,2] + 0.72 * image[:,:,1] + 0.21 * image[:,:,0]
gray_img = grayValue.astype(np.uint8)

cv.imshow("Original", image)
cv.imshow("GrayScale", gray_img)
cv.waitKey(0)
cv.destroyAllWindows()