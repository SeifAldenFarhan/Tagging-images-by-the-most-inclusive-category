from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMainWindow, QLabel
from qtconsole.qt import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from beta import beta
from secondPageGui import Ui_MainWindow
import directoryPath

class Ui_Form(object):
    def __init__(self):
      self.dirPath = ""
      self.images_group_list = []
      self.groups_description = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(778, 815)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(570, 62))
        self.label.setStyleSheet("\n""font: 75 italic 14pt \"Rockwell\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        spacerItem = QtWidgets.QSpacerItem(761, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.pushButton.clicked.connect(lambda: self.getPathFun() )
        spacerItem1 = QtWidgets.QSpacerItem(761, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.line_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.groups_number = QtWidgets.QSpinBox(Form)
        self.groups_number.setObjectName("groups_number")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.groups_number)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.line_3)

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.pushButton_5)
        self.pushButton_5.clicked.connect(lambda: self.classifyFunc())

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.line_5)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.line_4)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(lambda: self.viewPicFunc())

        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(lambda: self.wordCloudFunc())

        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.formLayout.setLayout(16, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.line_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">                    Welcome to SemanticPic</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Classify picture by labels, choose pictures path: </span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "browse.."))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Classification parameters</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "Classify"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Groups list</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">To see </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">the group</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">picture </span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "View Pictures"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">To see </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">the WordCloud </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">of group </span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "View WordCloud"))

    def getPathFun(self):
      a = directoryPath.App()
      self.dirPath = a.path
      print(self.dirPath)

    def classifyFunc(self):
      self.listWidget.setDisabled(False)
      self.listWidget.clear()
      beta().getDataFromES("labels")
      self.groups_description = beta().groupsDiscription(self.groups_number.value())
      self.images_group_list = beta().divideToGroups(self.groups_number.value())
      num = int(self.groups_number.text())
      for i in range(num):
        item = QListWidgetItem("Group %i" % (i + 1))
        self.listWidget.addItem(item)
      self.listWidget.show()

    @pyqtSlot()
    def viewPicFunc(self):
      group_number = self.listWidget.currentItem().text()[-1]
      num = int(group_number) - 1
      list_m = self.images_group_list[f"[{num}]"]
      list_m.append(group_number)
      self.ex = Ui_MainWindow()
      self.w = QtWidgets.QMainWindow()
      self.ex.setupUi(self.w, list_m, self.dirPath)
      self.w.show()

    def wordCloudFunc(self):
      item = {}
      group_number = self.listWidget.currentItem().text()[-1]
      num = int(group_number) - 1
      descriptionLength = len(self.groups_description[num])
      for i in range(15):
        item[f"{self.groups_description[num][i]}"] = 15 - i
      wordcloud = WordCloud(background_color="white").generate_from_frequencies(item)
      plt.figure()
      plt.imshow(wordcloud, interpolation="bilinear")
      plt.axis("off")
      plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
