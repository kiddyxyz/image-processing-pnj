import numpy, cv2 as cv, os

#img = numpy.zeros((11300, 11400), dtype=numpy.uint8)
img = numpy.zeros((230,230), dtype=numpy.uint8)
#image = img.reshape(300,400)
#image2 = img.shape

randomByteArray =  bytearray([
    255,255,255,0,0,0,255,255,255
],)
flatNumpyArray = numpy.array(randomByteArray)
print(flatNumpyArray)

# grayImage2 = flatNumpyArray.reshape(300,400)

cv.imwrite('RandomRunyeks.png', flatNumpyArray)