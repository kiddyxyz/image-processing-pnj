import numpy, cv2 as cv, os

grayImage = cv.imread("face.jpg", cv.IMREAD_GRAYSCALE)
imageResizer = cv.resize(grayImage,(300,400),3)

randomByteArray =  bytearray(imageResizer)
flatNumpyArray = numpy.array(randomByteArray)
print(flatNumpyArray)

grayImage2 = flatNumpyArray.reshape(300,400)

cv.imwrite('RandomRunyek.png', grayImage2)