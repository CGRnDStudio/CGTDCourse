==============================
Maya重命名工具
==============================

ls document讲解

import maya.cmds as cmds

def renameTool(pattern, targets):
    if not targets:
        cmds.warning("Please select at least one object")
        return None
    for target in targets:
        if not cmds.objExists(target):
            cmds.warning("%s is not exists" % target)
            continue
        print(target)
        cmds.rename(target, pattern)

rename("item", mc.ls(sl=True))

import maya.cmds as cmds

NUM_MATCH_SYMBOL = "#"

def renameTool(pattern, targets, start=1):
    """
    Naming function
        Arguments :
        pattern - str The naming pattern
        targets - list The need to renaming objects
        start - int The start number (default is 1)
    """
    newNameHead = ""
    newNameTail = ""
    # If start is negative, set it to zero
    if start < 0:
        start = 0
    # Find first sharp symbol position
    # If not found
    position = pattern.find(NUM_MATCH_SYMBOL)
    numberOfSharp = pattern.count(NUM_MATCH_SYMBOL)
    if position < 0:
        print("No \"#\" found, the number will suffix")
        newNameHead = pattern
        numberOfSharp = 1
    else:
        newNameHead = pattern.split(NUM_MATCH_SYMBOL)[0]
        newNameTail = "".join(pattern.split(NUM_MATCH_SYMBOL)[1:])
    counter = start
    for target in targets:
        if not cmds.objExists(target):
            continue
        newName = newNameHead
        newName += str(counter).zfill(numberOfSharp)
        newName += newNameTail
        cmds.rename(target, newName)
        counter += 1
    return True

renameTool("item_###_grp", cmds.ls(sl=True), 10)

如何写成package使用

python中执行mel
mel中执行python

#!/usr/bin/python
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
        self.setWindowTitle("Example")

if __name__ == "__main__":
    ex = Example()
    ex.show()


