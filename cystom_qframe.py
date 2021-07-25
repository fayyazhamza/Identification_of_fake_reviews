from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
import abc



class CustomQFrame(QFrame):

    def __init__(self, canUpdate: bool = False, updateInterVal: int = 1000,screenName: str = "",  parent=None, singleShot: bool = False,forceConnect=False):
        QFrame.__init__(self, parent=parent)
        self.forceConnect = forceConnect
        self.isSingleShot = singleShot
        self.screenName = screenName
        self.updateInterVal = updateInterVal
        self.canUpdate = canUpdate
        self.setContentsMargins(0, 0, 0, 0)
        self.initializeVars()
        self.setupVars()
        self.addVarsToLayout()
        self.timer = QTimer(self)

        if canUpdate:
            pass
            # self.ss: SharedSignals = SharedSignals.getInstance()
            # self.ss.currentTabNameSignal.connect(self.screenSwitch)
        if self.forceConnect:
            pass
            # if self.isSingleShot:
            #     QTimer.singleShot(self.updateInterVal,self.updateWidget)
            # else:
            #     self.timer.timeout.connect(self.updateWidget)
            #     self.timer.start(self.updateInterVal)

    @abc.abstractmethod
    def initializeVars(self):
        return

    @abc.abstractmethod
    def setupVars(self):
        return

    @abc.abstractmethod
    def addVarsToLayout(self):
        return

    def screenSwitch(self, screenName):
        if self.screenName == screenName:
            print("came to " + self.screenName)
            if self.isSingleShot:
                QTimer.singleShot(self.updateInterVal,self.updateWidget)
            else:
                self.timer.timeout.connect(self.updateWidget)
                self.timer.start(self.updateInterVal)
        else:
            print("going away from " + self.screenName)
            self.timer.stop()

    def updateWidget(self):
        pass