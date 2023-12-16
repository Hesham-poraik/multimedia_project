from PyQt5 import QtGui, QtWidgets, QtCore
from modify import modify_image

class Ui_main_layout(object):
  def setupUi(self, main_layout):
    main_layout.setObjectName("main_layout")
    main_layout.resize(1100, 630)
    main_layout.setStyleSheet("background: #f1f5f9")
    main_layout.setWindowIcon(QtGui.QIcon('assets/app.ico'))

    self.first = True
    self.gridLayout = QtWidgets.QGridLayout(main_layout)
    self.gridLayout.setContentsMargins(4, 4, 4, 4)
    self.gridLayout.setSpacing(0)
    self.gridLayout.setObjectName("gridLayout")

    # two state
    self.two_state = QtWidgets.QFrame(main_layout)
    self.two_state.setToolTipDuration(-1)
    self.two_state.setStyleSheet("max-width: 0")
    self.two_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.two_state.setFrameShadow(QtWidgets.QFrame.Raised)
    self.two_state.setLineWidth(1)
    self.two_state.setObjectName("two_state")

    self.gridLayout_2 = QtWidgets.QGridLayout(self.two_state)
    self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
    self.gridLayout_2.setSpacing(4)
    self.gridLayout_2.setObjectName("gridLayout_2")

    self.frame_2 = QtWidgets.QFrame(self.two_state)
    self.frame_2.setMinimumSize(QtCore.QSize(240, 0))
    self.frame_2.setMaximumSize(QtCore.QSize(242, 16777215))
    self.frame_2.setStyleSheet("background: #fff;border: 1px solid #aaa; border-radius: 10px;width: 240px;max-width: 240px;min-width: 240px;")
    self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame_2.setObjectName("frame_2")

    self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
    self.verticalLayout.setObjectName("verticalLayout")

    self.pushButton = QtWidgets.QPushButton(self.frame_2)
    self.pushButton.setStyleSheet("width: 220px;min-width: 220px;font-size: 21px;border: none")
    self.pushButton.setObjectName("pushButton")

    self.verticalLayout.addWidget(self.pushButton)
    spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.verticalLayout.addItem(spacerItem)

    self.pushButton_1 = QtWidgets.QPushButton(self.frame_2)
    self.pushButton_1.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_1.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_1.setObjectName("pushButton_1")
    self.pushButton_1.clicked.connect(lambda: self.modify_image('one'))
    self.verticalLayout.addWidget(self.pushButton_1)

    self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
    self.pushButton_2.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_2.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_2.setObjectName("pushButton_2")
    self.pushButton_2.clicked.connect(lambda: self.modify_image('two'))
    self.verticalLayout.addWidget(self.pushButton_2)

    self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
    self.pushButton_3.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_3.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_3.setObjectName("pushButton_3")
    self.pushButton_3.clicked.connect(lambda: self.modify_image('three'))
    self.verticalLayout.addWidget(self.pushButton_3)

    self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
    self.pushButton_4.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_4.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_4.setObjectName("pushButton_4")
    self.pushButton_4.clicked.connect(lambda: self.modify_image('four'))
    self.verticalLayout.addWidget(self.pushButton_4)

    self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
    self.pushButton_5.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_5.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_5.setObjectName("pushButton_5")
    self.pushButton_5.clicked.connect(lambda: self.modify_image('five'))
    self.verticalLayout.addWidget(self.pushButton_5)

    self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
    self.pushButton_6.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_6.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_6.setObjectName("pushButton_6")
    self.pushButton_6.clicked.connect(lambda: self.modify_image('six'))
    self.verticalLayout.addWidget(self.pushButton_6)

    self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
    self.pushButton_8.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_8.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_8.setObjectName("pushButton_8")
    self.pushButton_8.clicked.connect(lambda: self.modify_image('eight'))
    self.verticalLayout.addWidget(self.pushButton_8)

    self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
    self.pushButton_7.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_7.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_7.setObjectName("pushButton_7")
    self.pushButton_7.clicked.connect(lambda: self.modify_image('seven'))
    self.verticalLayout.addWidget(self.pushButton_7)

    spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.verticalLayout.addItem(spacerItem1)
    self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

    self.frame_3 = QtWidgets.QFrame(self.two_state)
    self.frame_3.setStyleSheet("background: #fff;border: 1px solid #aaa")
    self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame_3.setObjectName("frame_3")

    self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
    self.gridLayout_3.setObjectName("gridLayout_3")

    self.pushButton_down = QtWidgets.QPushButton(self.frame_3)
    self.pushButton_down.setMinimumSize(QtCore.QSize(0, 48))
    self.pushButton_down.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_down.setStyleSheet("width: 220px;min-width: 220px;background: #4611b1; font-size: 21px; color: #fff;")
    self.pushButton_down.setObjectName("pushButton_down")
    self.pushButton_down.clicked.connect(lambda: self.modify_image('down'))
    self.verticalLayout.addWidget(self.pushButton_down)

    self.img_label = QtWidgets.QLabel(self.frame_3)
    self.img_label.setAlignment(QtCore.Qt.AlignCenter)
    self.img_label.setStyleSheet("border: none")
    self.img_label.setMinimumSize(10, 10)
    self.gridLayout_3.addWidget(self.img_label, 0, 0, 1, 1)

    self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
    self.gridLayout.addWidget(self.two_state, 1, 0, 1, 1)

    # state one
    self.one_state = QtWidgets.QFrame(main_layout)
    self.one_state.setStyleSheet("background: #fff;border: 1px solid #aaa; border-radius: 10px;")
    self.one_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.one_state.setFrameShadow(QtWidgets.QFrame.Raised)
    self.one_state.setObjectName("one_state")

    self.gridLayout_4 = QtWidgets.QGridLayout(self.one_state)
    self.gridLayout_4.setObjectName("gridLayout_4")

    self.frame_4 = QtWidgets.QFrame(self.one_state)
    self.frame_4.setMaximumSize(QtCore.QSize(16777215, 300))
    self.frame_4.setStyleSheet("border:none")
    self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame_4.setObjectName("frame_4")

    self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
    self.gridLayout_6.setObjectName("gridLayout_6")

    self.pushButton_up = QtWidgets.QPushButton(self.frame_4)

    font = QtGui.QFont()
    font.setPointSize(-1)
    font.setBold(True)
    font.setWeight(75)

    self.pushButton_up.setFont(font)
    self.pushButton_up.setStyleSheet("font-size: 80px; color: #4611b1; border: none")
    self.pushButton_up.setObjectName("pushButton_up")

    self.gridLayout_6.addWidget(self.pushButton_up, 0, 0, 1, 1)
    self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1)

    self.frame = QtWidgets.QFrame(self.one_state)
    self.frame.setStyleSheet("border:none")
    self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame.setObjectName("frame")

    self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
    self.gridLayout_5.setObjectName("gridLayout_5")

    self.pushButton_upload = QtWidgets.QPushButton(self.frame)
    self.pushButton_upload.setMinimumSize(QtCore.QSize(0, 65))
    self.pushButton_upload.setMaximumSize(QtCore.QSize(400, 16777215))
    self.pushButton_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pushButton_upload.setStyleSheet("background: #4611b1; font-size: 28px; color: #fff;max-width: 400px")
    self.pushButton_upload.setObjectName("pushButton_upload")
    self.pushButton_upload.clicked.connect(self.upload_image)

    self.gridLayout_5.addWidget(self.pushButton_upload, 0, 0, 1, 1)
    self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)
    self.gridLayout.addWidget(self.one_state, 1, 1, 1, 1)

    self.retranslateUi(main_layout)
    QtCore.QMetaObject.connectSlotsByName(main_layout)

  def upload_image(self):
    # Open file dialog to select an image file
    fname, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', './assets/', 'Image files (*.png *.jpg *.jpeg)')

    # Update the image label with the selected image
    if fname:
        self.one_state.setStyleSheet("border-radius: 10px;max-width: 0")
        self.two_state.setStyleSheet("background: #f1f5f9;min-width: 100%")
        QtWidgets.QApplication.processEvents()
        self.fname = fname
        pixmap = QtGui.QPixmap(fname)
        target_size = self.img_label.size()
        scaled_pixmap = pixmap.scaled(target_size, QtCore.Qt.KeepAspectRatio)
        self.img_label.setPixmap(scaled_pixmap)

  def modify_image(self, jop):
    modify_image(self, jop)  

  def retranslateUi(self, main_layout):
        _translate = QtCore.QCoreApplication.translate
        main_layout.setWindowTitle(_translate("main_layout", "image processing"))
        main_layout.setWindowFilePath(_translate("main_layout", "background: #f1f5f9"))
        self.pushButton.setText(_translate("main_layout", "Edit your photo"))
        self.pushButton_1.setText(_translate("main_layout", "Original"))
        self.pushButton_2.setText(_translate("main_layout", "Rotate"))
        self.pushButton_3.setText(_translate("main_layout", "Sharp"))
        self.pushButton_4.setText(_translate("main_layout", "Blur"))
        self.pushButton_5.setText(_translate("main_layout", "Canny"))
        self.pushButton_6.setText(_translate("main_layout", "Emboss"))
        self.pushButton_7.setText(_translate("main_layout", "img → txt"))
        self.pushButton_8.setText(_translate("main_layout", "Mirror"))
        self.pushButton_down.setText(_translate("main_layout", "🕹️ save image"))
        self.pushButton_up.setText(_translate("main_layout", "Image Processing"))
        self.pushButton_upload.setText(_translate("main_layout", "Upload your image"))
