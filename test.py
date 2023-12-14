import cv2 as cv
  
img = cv.imread("test.jpg")

cv.imshow("image", img)
cv.imshow("mirror_image", img[:,::-1,:])
print(img.shape, img[:,::-1,:].shape)
cv.waitKey(0) 


# Setting parameter values 
t_lower = 50  # Lower Threshold 
t_upper = 150  # Upper threshold 
  
# Applying the Canny Edge filter 
# edge = cv.Canny(img, t_lower, t_upper) 
# edge.reshape(edge.shape[0], edge.shape[1], 1)
# cv.imshow('original', img) 
# print(edge.shape)
# print(len(edge.shape))
# cv.imshow('edge', edge) 
# cv.waitKey(0) 
# cv.destroyAllWindows()



# def convert_cv_image_to_pixmap(image):
#     height, width, x = image.shape
#     bytes_per_line = 1 * width
#     q_image = QtGui.QImage(image.data, width, height, bytes_per_line, QtGui.QImage.Format_Grayscale8)
#     return QtGui.QPixmap.fromImage(q_image)


    