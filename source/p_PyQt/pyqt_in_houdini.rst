=============================
PyQt在Houdini中执行的模板代码
=============================

PyQt的历史
Dialog、Layout与Widget之间的关系
setStyleSheet
load


https://build-system.fman.io/qt-designer-download
https://github.com/qt

.. code-block:: python

    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    """

    """

    import os
    import sys

    import re


    try:
        APP = "houdini"
        import hou

        from PySide2 import QtCore
        from PySide2 import QtWidgets as QtGui
    except Exception as e:
        raise


    class ActiveShotgun(QtGui.QDialog):
        """
        Initial main window
        """
        def __init__(self, parent=None):
            """
            """
            super(ActiveShotgun, self).__init__(parent)

            self._initUI()

        def _initUI(self):

            gbChoose = QtGui.QGroupBox("Choose Asset or Shot:")
            hblChoose = QtGui.QVBoxLayout()
            self.rbAsset = QtGui.QRadioButton("Asset")
            self.rbShot = QtGui.QRadioButton("Shot")
            self.rbShot.setChecked(True)
            hblChoose.addWidget(self.rbAsset)
            hblChoose.addWidget(self.rbShot)
            gbChoose.setFixedHeight(100)
            gbChoose.setLayout(hblChoose)

            # Initial labels
            hlLabel = QtGui.QHBoxLayout()
            lProj = QtGui.QLabel("Proj:")
            lTask = QtGui.QLabel("Task:")
            hlLabel.addWidget(lProj)
            hlLabel.addWidget(lTask)

            # Initial choose asset or shot task
            hlListWidget = QtGui.QHBoxLayout()
            self.lwProj = QtGui.QListWidget()

            self.lwTask = QtGui.QListWidget()
            hlListWidget.addWidget(self.lwProj)
            hlListWidget.addWidget(self.lwTask)

            # Initial buttons
            hlActive = QtGui.QHBoxLayout()
            pbActive = QtGui.QPushButton("&Active Shotgun...")
            pbActive.setFixedWidth(120)
            pbActive.setFixedHeight(50)
            hlActive.addStretch(1)
            hlActive.addWidget(pbActive)

            v_box = QtGui.QVBoxLayout()
            v_box.addWidget(gbChoose)
            v_box.addLayout(hlLabel)
            v_box.addLayout(hlListWidget)
            v_box.addLayout(hlActive)

            self.setLayout(v_box)
            self.resize(QtCore.QSize(500, 600))
            self.setWindowTitle("Active Shotgun Options: Hello, %s")
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        def closeEvent(self, event):
            self.done(0)


    def showUI(func):
        """
        Show UI instance
        """
        app = QtGui.QApplication.instance()

        if not app:
            app = QtGui.QApplication([APP])

        dialog = func()
        dialog.raise_()
        dialog.show()
        dialog.exec_()


    def main():
        """
        main function
        """
        showUI(ActiveShotgun)

    main()

.. code-block:: python

    import os
    import hou

    from hutil.Qt import QtCore, QtWidgets, QtUiTools
    from commonQt.appQss import qss
    path = os.path.dirname(__file__)
    print(path)


    class AttribManager(QtWidgets.QWidget):
        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            print("Hey I am in a class!!!")

            # load UI file
            loader = QtUiTools.QUiLoader()
            self.ui = loader.load("D:/centralizeTools/houdini/scripts/python/houQt/untitled.ui")

            # Layout
            mainLayout = QtWidgets.QVBoxLayout()
            mainLayout.setContentsMargins(0, 0, 0, 0)
            mainLayout.addWidget(self.ui)
            self.setLayout(mainLayout)
            self.setStyleSheet(qss)


    def show():
        dialog = AttribManager()
        dialog.setParent(hou.qt.floatingPanelWindow(None), QtCore.Qt.Window)
        dialog.show()


    if __name__ == "hou.session":
        show()


将.ui文件转.py文件

.. code-block:: bash

    C:\Python27\Scripts\pyside-uic.exe -o ???.py ???.ui

将.qrc文件转.py文件

.. code-block:: bash

    C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe -o ???.py ???.qrc

Python代码将.ui转.py文件

.. code-block:: python

    import pyside2uic

    with open("py文件路径", "w") as f:
        pyside2uic.compileUi("ui文件路径", f)

# load ui
