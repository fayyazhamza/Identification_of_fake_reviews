from PyQt5.QtWidgets import *


class ExceptionDialog(QDialog):

    def __init__(self, errText:str,header):
        super(ExceptionDialog, self).__init__()

        self.setWindowTitle(header)

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(errText))
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


def showMessageDialog(err:str, header="Error"):
    dlg = ExceptionDialog(errText=err, header=header)

    if dlg.exec_():
        print("Success!")
        return True
    else:
        print("Cancel!")
        return False