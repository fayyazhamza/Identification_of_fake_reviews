import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from Model import Classifier
from excpetionDialog import showMessageDialog
from helper_functions import convertQWidgetToCentredRow


class MainWindow(QMainWindow):
    EXIT_CODE_REBOOT = -123

    def __init__(self, parent=None):
        self.currentImagePath = ''
        self.currentText = ""
        QWidget.__init__(self, parent=parent)
        self.setWindowTitle("FYP ")
        self.classifier = Classifier()

        self.mainWidget = QWidget()
        self.mainColumn = QVBoxLayout()
        self.mainColumn.setAlignment(Qt.AlignCenter)

        self.responseLabel = QLabel()
        self.imageLabel = QLabel()
        self.imageLabel.mouseReleaseEvent = lambda e: self.onImageClicked()
        self.imagePixmap = QPixmap("assets/notfound.png")
        self.imagePixmap.scaled(640, 640,
                                transformMode=Qt.SmoothTransformation)
        self.imageLabel.setPixmap(self.imagePixmap)

        self.lineEdit = QPlainTextEdit()

        self.lineEdit.setMinimumHeight(200)
        self.submit = QPushButton("Submit")
        self.submit.clicked.connect(self.onSubmitClicked)

        self.mainColumn.addWidget(self.imageLabel)
        self.mainColumn.addWidget(self.lineEdit)
        self.mainColumn.addWidget(self.submit)
        self.mainColumn.addLayout(convertQWidgetToCentredRow(self.responseLabel))

        self.mainWidget.setLayout(self.mainColumn)
        self.setCentralWidget(self.mainWidget)
        self.show()

    def onSubmitClicked(self):

        self.currentText = self.lineEdit.toPlainText()
        if self.currentText == "":
            showMessageDialog(err="Can't have Empty text",header='Error')
            return
        try:
            response = self.classifier.inference(image=self.currentImagePath, text=self.currentText)
            if response:
                showMessageDialog(err='Genuine Review',header='Response')
                # self.responseLabel.setText("Genuine Review")
                # self.genuiineStyle(self.responseLabel)
            else:
                showMessageDialog(err='Fake Review',header='Response')

                # self.responseLabel.setText("Fake Review")
                # self.errorStyle(self.responseLabel)
            self.lineEdit.clear()
            self.imagePixmap = QPixmap("assets/notfound.png")
            self.imagePixmap.scaled(640, 480,
                                    transformMode=Qt.SmoothTransformation)
            self.imageLabel.setPixmap(self.imagePixmap)
        except Exception as e:
            print(e)

    def errorStyle(self, label: QLabel):
        label.setStyleSheet("""
        color: red;
        """)

    def genuiineStyle(self, label: QLabel):
        label.setStyleSheet("""
        color: green;
        """)

    def onImageClicked(self):
        try:

            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.ExistingFile)
            dlg.setNameFilters(["(*.JPG)", "(*.jpg)"])
            # filenames = QStringList()
            # print("browse clicked 1")
            if dlg.exec():
                # print("browse clicked 2")
                filenames = dlg.selectedFiles()
                # dlg.set
                # self.ss.closeCapWhileBrowsingSignal.emit(True)
                # print('file nmames')
                filename = list(filenames)
                if filename.__len__() > 0:
                    # print( )
                    # pass
                    self.currentImagePath = filename[0]
                    self.imagePixmap = QPixmap(filename[0])
                    self.imagePixmap.scaled(640, 480, aspectRatioMode=Qt.KeepAspectRatioByExpanding,
                                            transformMode=Qt.SmoothTransformation)
                    self.imageLabel.setPixmap(self.imagePixmap)

            else:
                print("no files slected")

            dlg.close()
        except:
            print("Browsing Failed")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    sys.exit(app.exec_())
