=============================
PyQt信号与槽事件机制
=============================

- 事件无处不在，默认都有一套事件机制，可以重写来修改事件
- 控件都有自己的信号函数和对应的信号处理函数
- 事件比较隐蔽，一般很难察觉
- 在MVC编辑代码的时候，事件机制很复杂
- qss也是，自有的一套事件机制

.. code-block:: python

    import sys
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
        QVBoxLayout, QApplication)


    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):

            lcd = QLCDNumber(self)
            sld = QSlider(Qt.Horizontal, self)

            vbox = QVBoxLayout()
            vbox.addWidget(lcd)
            vbox.addWidget(sld)

            self.setLayout(vbox)
            sld.valueChanged.connect(lcd.display)

            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Signal and slot')
            self.show()


    if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

.. code-block:: python

    import sys
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QWidget, QApplication

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):      

            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Event handler')
            self.show()


        def keyPressEvent(self, e):

            if e.key() == Qt.Key_Escape:
                self.close()


    if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())


.. code-block:: python

    import sys
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):      

            grid = QGridLayout()
            grid.setSpacing(10)

            x = 0
            y = 0

            self.text = "x: {0},  y: {1}".format(x, y)

            self.label = QLabel(self.text, self)
            grid.addWidget(self.label, 0, 0, Qt.AlignTop)

            self.setMouseTracking(True)

            self.setLayout(grid)

            self.setGeometry(300, 300, 350, 200)
            self.setWindowTitle('Event object')
            self.show()


        def mouseMoveEvent(self, e):

            x = e.x()
            y = e.y()

            text = "x: {0},  y: {1}".format(x, y)
            self.label.setText(text)


    if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


    class Example(QMainWindow):

        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):      

            btn1 = QPushButton("Button 1", self)
            btn1.move(30, 50)

            btn2 = QPushButton("Button 2", self)
            btn2.move(150, 50)

            btn1.clicked.connect(self.buttonClicked)            
            btn2.clicked.connect(self.buttonClicked)

            self.statusBar()

            self.setGeometry(300, 300, 290, 150)
            self.setWindowTitle('Event sender')
            self.show()


        def buttonClicked(self):

            sender = self.sender()
            self.statusBar().showMessage(sender.text() + ' was pressed')


    if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

自定义信号发射

.. code-block:: python

    import sys
    from PyQt5.QtCore import pyqtSignal, QObject
    from PyQt5.QtWidgets import QMainWindow, QApplication


    class Communicate(QObject):

        closeApp = pyqtSignal() 


    class Example(QMainWindow):

        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):

            self.c = Communicate()
            self.c.closeApp.connect(self.close)

            self.setGeometry(300, 300, 290, 150)
            self.setWindowTitle('Emit signal')
            self.show()


        def mousePressEvent(self, event):

            self.c.closeApp.emit()


    if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

.. code-block:: python

    import sys

    path = "D:/2020"

    path in sys.path or sys.path.insert(0, path)

    from PySide2 import QtWidgets
    from PySide2 import QtGui
    from PySide2 import QtCore
    import mainWin

    class CustomDialog(QtWidgets.QDialog, mainWin.Ui_Dialog):
        def __init__(self, parent=None):
            super(CustomDialog, self).__init__(parent)

            self.setupUi(self)

        @QtCore.Slot()
        def on_pushButton_clicked(self):
            print(100)

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        dialog = CustomDialog()
        dialog.show()
        sys.exit(app.exec_())
