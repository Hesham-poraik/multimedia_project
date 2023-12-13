import sys
import pyqt_ui

if __name__ == "__main__":
    app = pyqt_ui.QtWidgets.QApplication(sys.argv)
    main_layout = pyqt_ui.QtWidgets.QWidget()
    ui = pyqt_ui.Ui_main_layout()
    ui.setupUi(main_layout)
    main_layout.show()
    sys.exit(app.exec_())