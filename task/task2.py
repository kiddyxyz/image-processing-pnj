import numpy, cv2 as cv, os

#img = numpy.zeros((11300, 11400), dtype=numpy.uint8)
#img = numpy.zeros((230,230), dtype=numpy.uint8)
#image = img.reshape(300,400)
#image2 = img.shape
# Create a black image
img = numpy.zeros((212,212,3), numpy.uint8)
cv.line(img,(20,110),(490,110),(255,255,255),5)
cv.imwrite('white-line.png', img)