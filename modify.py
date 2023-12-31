import cv2 as cv
from PyQt5 import QtGui, QtCore
import os
import numpy as np
# import easyocr

"""
@param self.fname: local path for image on user devise
@param self.download: binary image variable can for save image
@param edited_pixmap: pixel map image to display on pyqt
"""
def modify_image(self, jop):
  # read image 
  if(self.first): # self.first = True
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
      Image2String(self, image)
      self.download = image
    case "eight":
      new_image = mirror(image)
      display(self, new_image)
    case "down":
      if self.download is not None:
        output_path = os.path.join(os.path.dirname(self.fname), "output/output.jpg")
        cv.imwrite(output_path, self.download)
    case "change":
        self.one_state.setStyleSheet("background: #ffffff;border: 1px solid #aaa; border-radius: 10px;width: 100%; min-width: 100%: max-width: 100%;")
        self.two_state.setStyleSheet("background: #f1f5f9;min-width: 0; width: 0; max-width: 0")
        self.first = True
    case _:
      # write your implementation
      print("what are you want [*_*]")

def convert_cv_image_to_pixmap(image, target_size):
    if len(image.shape) == 2:#[255, 255]
        height, width = image.shape
        bytes_per_line = 1 * width
        q_image = QtGui.QImage(image.data.tobytes(), width, height, bytes_per_line, QtGui.QImage.Format_Grayscale8)
    else:
        height, width, channels = image.shape#[256, 256, 3]
        bytes_per_line = channels * width
        q_image = QtGui.QImage(image.data.tobytes(), width, height, bytes_per_line, QtGui.QImage.Format_BGR888)
        
    return QtGui.QPixmap.fromImage(q_image.scaled(target_size, QtCore.Qt.KeepAspectRatio))

# change image on pyqt
def display(self, final_image):
    self.download = final_image
    target_size = self.img_label.size()
    edited_pixmap = convert_cv_image_to_pixmap(final_image, target_size)
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
    emboss_img = cv.filter2D(image, -1, emboss_kernel)
    return emboss_img

def mirror(image):
    if(len(image.shape)==3):
      return image[:,::-1,:]
    elif(len(image.shape)==2):
      return image[:,::-1]

def Image2String(self, image):
    # Inctance Text Detector
    reader = easyocr.Reader(['en'], gpu=False)
    # # Detect Text in Image
    text_ = reader.readtext(image)
    #***********************
    text:str = ""
    for line in text_:
        text += line[1] + "\n"#[,,]
    # Create File
    output_path = r"./assets/output/textfile.txt"
    try:
      os.remove(output_path)
    except:
      pass
    myfile = open(output_path, "a")
    # with open(output_path, "a") as myfile:
    myfile.write(text)
    myfile.close()