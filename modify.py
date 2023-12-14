import cv2 as cv
from PyQt5 import QtGui
import os
import numpy as np

"""
@param self.fname: local path for image on user devise
@param self.download: binary image variable can for save image
@param edited_pixmap: pixel map image to display on pyqt
"""
def modify_image(self, jop):
  # read image
  if(self.first):
      image = cv.imread(self.fname, 1)
      self.first = False
  else:
      image = self.download

  match jop:
    case "one":
      binary_image = cv.imread(self.fname)
      display(self, binary_image)
    case "two":
      rotating_image = rotate(image)
      display(self, rotating_image)
    case "three":
      new_image = equalize_color_image(image)
      display(self, new_image)
    case "four":
      new_image = blur(image)
      display(self, new_image)
    case "five":
      new_image = canny(image)
      display(self, new_image)
    case "six":
      new_image = emboss(image)
      display(self, new_image)
    case "seven":
      Image2String(image)
    case "eight":
      new_image = mirror(image)
      display(self, new_image)
    case "down":
      if self.download is not None:
        output_path = os.path.join(os.path.dirname(self.fname), "output.jpg")
        cv.imwrite(output_path, self.download)
    case _:
      # write your implementation
      print("what are you want [*_*]")

def convert_cv_image_to_pixmap(image):
    if len(image.shape) == 2:
        height, width = image.shape
        bytes_per_line = 1 * width
        q_image = QtGui.QImage(image.data.tobytes()       , width, height, bytes_per_line, QtGui.QImage.Format_Grayscale8)
    else:
        height, width, channels = image.shape
        bytes_per_line = channels * width
        q_image = QtGui.QImage(image.data.tobytes(), width, height, bytes_per_line, QtGui.QImage.Format_BGR888)
        
    return QtGui.QPixmap.fromImage(q_image)

# change image on pyqt
def display(self, final_image):
    self.download = final_image
    edited_pixmap = convert_cv_image_to_pixmap(final_image)
    self.img_label.setPixmap(edited_pixmap)


# function filters
def rotate(image):
    rotating_image = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
    return rotating_image

def equalize_color_image(image):
    #  Python Program to sharp image 
    kernel = np.array( [[-1,-1,-1],
                        [-1, 9,-1],
                        [-1,-1,-1]])
    sharpened = cv.filter2D(image, -1, kernel)
    return sharpened

def blur(image):
    blurImg = cv.blur(image,(5,5))
    return blurImg

def canny(image):
    edge = cv.Canny(image, 50, 150)
    inverted_image = cv.bitwise_not(edge)
    # inverted_image = 255-edge
    return inverted_image

def emboss(image):
    emboss_kernel = np.array([[-1, 0, 0], 
                              [0, 0, 0], 
                              [0, 0, 1]]) 
    emboss_img = cv.filter2D(src=image, ddepth=-1, kernel=emboss_kernel)
    return emboss_img

def mirror(image):
    return image[:,::-1,:]




def Image2String(image):
    print("nothing to do!! (⓿_⓿)")
