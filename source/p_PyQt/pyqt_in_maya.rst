=============================
PyQt在Maya中执行的模板代码
=============================

坐井观天：本节知识点
如何用PyQt创建用户界面？
如何删除已经存在的用户界面？
如何给button连接函数传参？


管中窥豹：延伸阅读

from PySide2 import QtWidgets as QtGui

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self._initUI()
        
    def _initUI(self):
        pass
        
if __name__ == "__main__":
    dialog = MyDialog()
    dialog.show()

import maya.cmds as cmds
from PySide2 import QtWidgets as QtGui

DIALOGNAME = "My Dialog"

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self._initUI()
        
    def _initUI(self):
        self.setObjectName(DIALOGNAME)
        

if __name__ == "__main__":
    if cmds.window(DIALOGNAME, exists=True, query=True):
        cmds.deleteUI(DIALOGNAME)

    dialog = MyDialog()
    dialog.show()



#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from PySide import QtGui
    from PySide import QtCore
except ImportError:
    from PySide2 import QtWidgets as QtGui

class Example(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 500, 500)
        self.setWindowTitle("360 Playblast")
        Browse_Button = QtGui.QPushButton("Browse")
        name_label_file = QtGui.QLabel("Open file")
        self.name_line_edit_file = QtGui.QLineEdit()
        name_label_Frame = QtGui.QLabel("From")
        self.name_line_edit_frame = QtGui.QLineEdit()
        name_label_to = QtGui.QLabel("To")
        self.name_line_edit_to = QtGui.QLineEdit()
        name_label_Format = QtGui.QLabel("Format")
        self.ComboBox_format = QtGui.QComboBox()
        self.ComboBox_format.addItems(["avi", "image", "qt", "movie"])
        name_label_resolution = QtGui.QLabel("Resoultion")
        self.ComboBox_resolution = QtGui.QComboBox()
        self.ComboBox_resolution.addItems(["1920*1080", "1080*720", "720*540"])
        Browse_Button_to = QtGui.QPushButton("Browse")
        name_label_to1 = QtGui.QLabel("To")
        self.name_line_edit_file1 = QtGui.QLineEdit()
        name_button_OK = QtGui.QPushButton("OK")
        name_button_Canle = QtGui.QPushButton("Canle")
        baseLayout = QtGui.QGridLayout()
        baseLayout.addWidget(Browse_Button, 0, 2)
        baseLayout.addWidget(name_label_file, 0, 0)
        baseLayout.addWidget(self.name_line_edit_file, 0, 1)
        baseLayout.addWidget(name_label_Frame, 1, 0)
        baseLayout.addWidget(self.name_line_edit_frame, 1, 1)
        baseLayout.addWidget(name_label_to, 1, 2)
        baseLayout.addWidget(self.name_line_edit_to, 1, 3)
        baseLayout.addWidget(name_label_Format, 2, 0)
        baseLayout.addWidget(self.ComboBox_format, 2, 1)
        baseLayout.addWidget(name_label_resolution, 3, 0)
        baseLayout.addWidget(self.ComboBox_resolution, 3, 1)
        baseLayout.addWidget(name_label_to1, 4, 0)
        baseLayout.addWidget(self.name_line_edit_file1, 4, 1)
        baseLayout.addWidget(Browse_Button_to, 4, 2)
        baseLayout.addWidget(name_button_OK, 5, 1)
        baseLayout.addWidget(name_button_Canle, 5, 3)
        self.setLayout(baseLayout)

if __name__ == "__main__":
    ex = Example()
    ex.show()




from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
import maya.cmds as cmds

from PySide2.QtWidgets import *
# 命名污染 

from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

def getMayaMainWin():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(long(pointer), QtWidgets.QWidget)

mayaWindow = getMayaMainWin()
mayaWindow.setWindowOpacity(1)

class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=getMayaMainWin()):
        super(MyWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My Custom Window")
        self.setMinimumSize(QSize(360, 240))
        mainLayout = QtWidgets.QVBoxLayout()
        titleLabel = QLabel("Control Window")
        nameText = QLineEdit()
        execButton = QPushButton("Do It!")
        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(nameText)
        mainLayout.addWidget(execButton)
        self.setLayout(mainLayout)

        execButton.clicked.connect(self.createCube)

    def createCube(self):
        userInput = nameText.text()
        if not userInput:
            print("Please enter cube name!")
            return 0
        cubeName = cmds.polyCube?????
        print("%s has been created" % cubeName)

if "myWin" in globals():
    print("myWin is exists, close it first!")
    myWin.deleteLater()
    del mywin

myWin = MyWindow()
myWin.show()


理解类继承
查看PyQt文档
字符串格式化两种方法
理解类self

判断语句

真假事件
布尔运算 and or not bool()

PySide与PySide2的兼容性

if int(cmds.about(v=True)) >= 2017:
    from PySide2 import QtCore
    from PySide2 import QtGui as QtGui4
    from PySide2 import QtWidgets as QtGui
    from shiboken2 import wrapInstance
else:
    from PySide import QtGui
    from PySide import QtCore
    from shiboken import wrapInstance


loadUi


from functools import partial

def test(a, b, c):
    print(a, b, c)

f = partial(test, b=2, c=3)
f(100)
f = partial(test, 1, c=3)
f(100)



