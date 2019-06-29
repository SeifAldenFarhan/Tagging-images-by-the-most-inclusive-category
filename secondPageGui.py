import os.path
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QBoxLayout
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, photo_list, dirPath):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setFixedHeight(900)
        self.lay_m = QVBoxLayout(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.display_photo(photo_list, dirPath)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def display_photo(self, photo_list, dirPath):
      photo_num = len(photo_list)
      global lay
      for i in range(photo_num):
        if (i % 4) == 0:
          lay = QHBoxLayout(self.centralwidget)
          self.lay_m.addLayout(lay)
        label = QLabel(self.centralwidget)
        if os.path.exists(f'{dirPath}\{photo_list[i]}'):
          pixmap = QPixmap(f'C:\\Users\seif alden\Desktop\\final project\אלפא\photos\{photo_list[i]}')
          label.setPixmap(pixmap)
          label.setFixedSize(250, 250)
          lay.addWidget(label)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


photo_list = []
path = ""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w, photo_list, path)
    w.show()
    sys.exit(app.exec_())
