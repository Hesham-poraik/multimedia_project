import cv2 as cv
from PyQt5 import QtGui
import os

"""
@param self.fname: local path for image on user devise
"""
def modify_image(self, jop):
  match jop:
    case "one":
      binary_image = cv.imread(self.fname)
      self.download = binary_image
      edited_pixmap = QtGui.QPixmap(self.fname)
      self.img_label.setPixmap(edited_pixmap)
    case "two":
      # filtering image
      binary_image = cv.imread(self.fname, 0)
      self.download = binary_image
      # convert to pixmap image
      edited_pixmap = convert_cv_image_to_pixmap(binary_image)
      # update value on ui class
      self.img_label.setPixmap(edited_pixmap)
    case "three":
      # write your implementation
      print("three", self.fname)
    case "four":
      # write your implementation
      print("four", self.fname)
    case "five":
      # write your implementation
      print("five", self.fname)
    case "six":
      # write your implementation
      print("six", self.fname)
    case "seven":
      # write your implementation
      print("seven", self.fname)
    case "down":
      if self.download is not None:
        output_path = os.path.join(os.path.dirname(self.fname), "output.jpg")
        cv.imwrite(output_path, self.download)
    case _:
      # write your implementation
      print("what are you want [*_*]")


def convert_cv_image_to_pixmap(image):
    height, width = image.shape
    bytes_per_line = 1 * width
    q_image = QtGui.QImage(image.data, width, height, bytes_per_line, QtGui.QImage.Format_Grayscale8)
    return QtGui.QPixmap.fromImage(q_image)