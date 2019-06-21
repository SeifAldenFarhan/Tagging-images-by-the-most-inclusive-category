import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class App(QWidget):

  def __init__(self):
    super().__init__()
    self.title = 'Choice file ...'
    self.left = 20
    self.top = 20
    self.width = 840
    self.height = 650
    self.path = "None"
    self.initUI()

  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)
    self.openFileNameDialog()
    self.show()

  def openFileNameDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    dirName = QFileDialog.getExistingDirectory(self, options=options)

    if dirName:
      self.path = dirName
      # print(dirName)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = App()
  sys.exit(app.exec_())
