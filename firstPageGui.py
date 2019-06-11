from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMainWindow, QLabel
from qtconsole.qt import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from beta import beta
from secondPageGui import Ui_MainWindow

class Ui_Form(object):
  def setupUi(self, Form):
    Form.setObjectName("Form")
    Form.resize(640, 560)
    self.images_group_list = []

    self.submit = QtWidgets.QPushButton(Form)
    self.submit.setGeometry(QtCore.QRect(30, 160, 101, 31))
    self.submit.clicked.connect(lambda: self.submitFun())

    self.submit.setObjectName("submit")

    self.checkPhotos = QtWidgets.QPushButton(Form)
    self.checkPhotos.setGeometry(QtCore.QRect(300, 350, 175, 31))
    self.checkPhotos.clicked.connect(lambda: self.checkPhotosFun())
    self.checkPhotos.setObjectName("checkPhotos")

    self.line = QtWidgets.QFrame(Form)
    self.line.setGeometry(QtCore.QRect(20, 200, 481, 20))
    self.line.setFrameShape(QtWidgets.QFrame.HLine)
    self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line.setObjectName("line")

    self.listWidget = QtWidgets.QListWidget(Form)
    self.listWidget.setGeometry(QtCore.QRect(30, 230, 151, 270))
    self.listWidget.setObjectName("listWidget")
    self.listWidget.setDisabled(True)

    self.widget = QtWidgets.QWidget(Form)
    self.widget.setGeometry(QtCore.QRect(20, 30, 471, 81))
    self.widget.setObjectName("widget")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.verticalLayout = QtWidgets.QVBoxLayout()
    self.verticalLayout.setObjectName("verticalLayout")
    self.label = QtWidgets.QLabel(self.widget)
    self.label.setMaximumSize(QtCore.QSize(230, 53))
    self.label.setObjectName("label")
    self.verticalLayout.addWidget(self.label)
    self.label_name = QtWidgets.QComboBox(self.widget)
    self.label_name.setObjectName("label_name")
    self.label_name.addItem("")
    self.label_name.addItem("")
    self.label_name.addItem("")
    self.label_name.addItem("")
    self.label_name.addItem("")
    self.label_name.addItem("")
    self.verticalLayout.addWidget(self.label_name)
    self.horizontalLayout.addLayout(self.verticalLayout)
    self.verticalLayout_2 = QtWidgets.QVBoxLayout()
    self.verticalLayout_2.setObjectName("verticalLayout_2")
    self.groups_number_label = QtWidgets.QLabel(self.widget)
    self.groups_number_label.setObjectName("groups_number_label")
    self.verticalLayout_2.addWidget(self.groups_number_label)
    self.groups_number = QtWidgets.QSpinBox(self.widget)
    self.groups_number.setObjectName("groups_number")
    self.verticalLayout_2.addWidget(self.groups_number)
    self.horizontalLayout.addLayout(self.verticalLayout_2)

    self.retranslateUi(Form)
    self.submit.clicked.connect(self.listWidget.update)
    QtCore.QMetaObject.connectSlotsByName(Form)

  def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "Form"))
    self.submit.setText(_translate("Form", "Submit"))
    self.checkPhotos.setText(_translate("Form", "Check Photos"))
    __sortingEnabled = self.listWidget.isSortingEnabled()

    self.listWidget.setSortingEnabled(__sortingEnabled)
    self.label.setText(_translate("Form",
                                  "<html><head/><body><p><span style=\" font-size:9pt;\">Chose the label:</span></p></body></html>"))
    self.label_name.setItemText(0, _translate("Form", "labels"))
    self.label_name.setItemText(1, _translate("Form", "landmarks"))
    self.label_name.setItemText(2, _translate("Form", "logos"))
    self.label_name.setItemText(3, _translate("Form", "web"))
    self.label_name.setItemText(4, _translate("Form", "faces"))
    self.label_name.setItemText(5, _translate("Form", "text"))
    self.groups_number_label.setText(_translate("Form",
                                                "<html><head/><body><p><span style=\" "
                                                "font-size:9pt;\">Number of groups:</span></p></body></html>"))

  def submitFun(self):
    # b = beta()
    # print(self.label_name.currentText(), self.groups_number.value())
    beta().getDataFromES(self.label_name.currentText())
    self.images_group_list = beta().divideToGroups(self.groups_number.value())
    self.listWidget.setDisabled(False)
    self.listWidget.clear()
    num = int(self.groups_number.text())
    for i in range(num):
      item = QListWidgetItem("Group %i" % (i + 1))
      self.listWidget.addItem(item)
    self.listWidget.show()

  @pyqtSlot()
  def checkPhotosFun(self):
    group_number = self.listWidget.currentItem().text()[-1]
    list_m = self.images_group_list[f'[{int(group_number) - 1}]']
    list_m.append(group_number)

    self.ex = Ui_MainWindow()
    self.w = QtWidgets.QMainWindow()
    self.ex.setupUi(self.w, list_m)
    self.w.show()

if __name__ == "__main__":
  import sys
  app = QtWidgets.QApplication(sys.argv)
  Form = QtWidgets.QWidget()
  ui = Ui_Form()
  ui.setupUi(Form)
  Form.thread()
  Form.show()
  sys.exit(app.exec_())
