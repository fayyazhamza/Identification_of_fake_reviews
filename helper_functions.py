import json
import os
import re
from glob import glob

from PyQt5.QtWidgets import *

# todo delete from column method

def convertQWidgetToCentredRow(widgetToConvert: QWidget) -> QHBoxLayout:
    row = QHBoxLayout()
    # row.setAlignment(Qt.AlignCenter)
    row.setContentsMargins(0, 0, 0, 0)
    row.addStretch(1)
    row.addWidget(widgetToConvert)
    row.addStretch(1)
    return row

def convertQWidgettoLeadingRow(widgetToConvert: QWidget, stretch: int = 1,spacing=0) -> QHBoxLayout:
    row = QHBoxLayout()
    # row.setAlignment(Qt.AlignCenter)
    # todo add asertion if asertion greater then 100
    row.setContentsMargins(0, 0, 0, 0)
    if stretch == 1:
        row.addSpacing(spacing)
        row.addWidget(widgetToConvert)
        row.addStretch(stretch)
    else:
        row.addWidget(widgetToConvert, stretch)
        row.addStretch(100 - 20)
    return row


def convertQWidgettoTrailingRow(widgetToConvert: QWidget, stretch: int = 1) -> QHBoxLayout:
    row = QHBoxLayout()
    # row.setAlignment(Qt.AlignCenter)
    # todo add asertion if asertion greater then 100
    row.setContentsMargins(0, 0, 0, 0)
    if stretch == 1:
        row.addStretch(stretch)
        row.addWidget(widgetToConvert)
    else:
        row.addStretch(100 - 20)
        row.addWidget(widgetToConvert, stretch)
    return row

def deleteElementsinLayout(layout):
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                # child.widget().deleteLater()
                print("deleting sub coluimn")
                child.widget().setParent(None)
                # child.widget()
            elif child.layout() is not None:
                pass


def checkIfFileExists(filePath: str) -> bool:
    if os.path.isfile(filePath):
        return True
    else:
        return False

def checkIfFilenameContainingStringExists(filePath: str) -> bool:
    if glob(filePath):
        return True
    else:
        return False

def deleteFileIfExists(filepath):
    if checkIfFileExists(filepath):
        os.remove(filepath)

def getFilesWithPartialStringMatch(filepath):
    filenameList =[]
    if glob(filepath):
        fileList = glob(filepath)
        for file in fileList:
            filenameList.append(file.split("\\")[1])
    print(filenameList)
    return filenameList

def getTranslationLanguage(fileName):
    print(fileName)
    fileName = fileName.split('-')
    translationLanguage = fileName[1].rstrip(".txt")
    print(translationLanguage)
    return translationLanguage

def createDirectoryIfNotExists(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def createDirectories(paths):
    assert isinstance(paths, list)
    for path in paths:
        createDirectoryIfNotExists(path)

def createFileIfNotExists(path):
    if not os.path.isfile(path):
        with open(path,'w+'):
            pass

def overWriteJson(path,data):

    if checkIfFileExists(path):
        with open(path,'w+') as fp:
            json.dump(data,fp)

