==============================
Houdini用户界面
==============================

.. code-block:: python

    import hou

    from hutil.Qt import QtCore
    from hutil.Qt import QtWidgets
    from hutil.Qt import QtUiTools

    uiPath = "D:/centralizeTools/houdini/scripts/python/houQt/untitled.ui"

    class SnippetA(QtWidgets.QDialog):
        # self.ui only Main Window
        def __init__(self, parent=None):
            super(SnippetA, self).__init__(parent)

            # load UI file
            loader = QtUiTools.QUiLoader()
            self.ui = loader.load(uiPath)

            # Layout
            mainLayout = QtWidgets.QVBoxLayout()
            mainLayout.setContentsMargins(0, 0, 0, 0)
            mainLayout.addWidget(self.ui)
            self.setLayout(mainLayout)


    def show():
        dialog = SnippetA()
        dialog.show()
        dialog.exec_()


    if __name__ == "__builtin__":
        show()

.. code-block:: python

    import hou

    from hutil.Qt import QtCore
    from hutil.Qt import QtWidgets
    from hutil.Qt import QtUiTools

    uiPath = "D:/centralizeTools/houdini/scripts/python/houQt/untitled.ui"

    class SnippetB(QtWidgets.QDialog):
        def __init__(self, parent=None):
            super(SnippetB, self).__init__(parent)

            # load UI file
            loader = QtUiTools.QUiLoader()
            self.ui = loader.load(uiPath)

            # Layout
            mainLayout = QtWidgets.QVBoxLayout()
            mainLayout.setContentsMargins(0, 0, 0, 0)
            mainLayout.addWidget(self.ui)
            self.setLayout(mainLayout)


    def show():
        dialog = SnippetB()
        dialog.setParent(hou.qt.floatingPanelWindow(None), QtCore.Qt.Window)
        dialog.show()


    if __name__ == "__builtin__":
        show()

.. code-block:: python

    import hou

    from hutil.Qt import QtCore
    from hutil.Qt import QtWidgets
    from hutil.Qt import QtUiTools

    uiPath = "D:/centralizeTools/houdini/scripts/python/houQt/untitled.ui"

    class SnippetC(QtWidgets.QDialog):
        def __init__(self, parent=None):
            super(SnippetC, self).__init__(parent)

            # load UI file
            loader = QtUiTools.QUiLoader()
            self.ui = loader.load(uiPath)

            # Layout
            mainLayout = QtWidgets.QVBoxLayout()
            mainLayout.setContentsMargins(0, 0, 0, 0)
            mainLayout.addWidget(self.ui)
            self.setLayout(mainLayout)


    def show():
        dialog = SnippetC(hou.qt.floatingPanelWindow(None))
        dialog.show()


    if __name__ == "__builtin__":
        show()

.. code-block:: python

    import hou
    from hutil.Qt import QtCore
    from hutil.Qt import QtWidgets
    from houQt import mainWin
    reload(mainWin)


    class WindowA(QtWidgets.QMainWindow, mainWin.Ui_MainWindow):
        def __init__(self, parent=None):
            super(WindowA, self).__init__(parent)
            self.setupUi(self)


    def show():
        win = WindowA(hou.qt.floatingPanelWindow(None))
        win.show()
        win.exec_()

    if __name__ == "__builtin__":
        show()

.. code-block:: python

    from hutil.Qt import QtCore
    from hutil.Qt import QtWidgets
    from houQt import mainDialog
    reload(mainDialog)


    class WindowB(QtWidgets.QDialog, mainDialog.Ui_Dialog):
        def __init__(self, parent=None):
            super(WindowB, self).__init__(parent)
            self.setupUi(self)


    def show():
        win = WindowB(hou.qt.floatingPanelWindow(None))
        win.show()

    if __name__ == "__builtin__":
        show()