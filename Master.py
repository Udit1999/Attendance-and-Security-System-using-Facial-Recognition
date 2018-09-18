
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QAbstractButton, QVBoxLayout, QMessageBox ,QLineEdit, QMainWindow)
from PyQt5 import QtGui , QtCore
from PyQt5.QtGui import *
import FaceDetection
import detector
import dataSetGenerator
import trainer

class WebCam(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Alert'
        self.left = 900
        self.top = 200
        self.width = 320
        self.height = 200

    def initUI(self,n):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        icn = QtGui.QIcon()
        icn.addPixmap(QtGui.QPixmap("alert.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icn)


        buttonReply = QMessageBox.question(self, 'ALERT!!!', "Do you like to open webcam?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            if n==1:
                FaceDetection.faceDetection()
            elif n==2:
                dataSetGenerator.DSGen()
                trainer.train()
            else:
                detector.predictor()
        self.show()



def fd():

    app = QApplication(sys.argv)
    ex  = WebCam()
    ex.initUI(1)
    sys.exit(app.exec_())


def train():
    print("Train")
    app = QApplication(sys.argv)
    ex  = WebCam()
    ex.initUI(2)
    sys.exit(app.exec_())

def predict():
    print("Predict")
    app = QApplication(sys.argv)
    ex  = WebCam()
    ex.initUI(3)
    sys.exit(app.exec_())


class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #grid = QGridLayout()
        grid = QVBoxLayout()
        self.setLayout(grid)

        button_fd = PicButton(QPixmap('Face-detection.png'),self)
        button_fd.setToolTip("Detects Face and Eyes")
        button_fd.clicked.connect(fd)

        button_t = PicButton(QPixmap('train.jpeg'),self)
        button_t.setToolTip("Trains the system for new face")
        button_t.clicked.connect(train)

        button_fr = PicButton(QPixmap('face-recognition.png'),self)
        button_fr.setToolTip("Predicts the Face ID")
        button_fr.clicked.connect(predict)

        grid.addWidget(button_fd)
        grid.addWidget(button_t)
        grid.addWidget(button_fr)


        self.move(300, 150)
        self.setWindowTitle('Face Detector')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Face-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setWindowIcon(icon)
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
