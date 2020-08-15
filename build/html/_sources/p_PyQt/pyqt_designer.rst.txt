=============================
PyQt Designer安装与使用
=============================

了解PyQt的历史以及协议，Qt实际是C++的一套GUI编程的套件，底层就是C++ Qt，Python将其做了封装之后才有了PyQt的UI库。

- Qt4->PyQt4->PySide
- Qt5->PyQt5->PySide2

PySide和PyQt实际是一回事，只是开源协议有所不同，从我使用的角度来说有些高级功能可能不太一样，比如数据库的支持，比如uic的支持，最新版本的Houdini、Maya与Nuke中内置PySide2，以前老版本是内置PySide，内置使用起来就比较方便，当然你非得使用PyQt5，就得基于具体的软件的Python环境去编译一套PyQt库来使用。

PyQt5和PySide2可以直接通过pip安装即可，如果有特殊版本得费点心思，一般安装好PySide2，你就可以找到这个C:\Python37\Lib\site-packages\PySide2\designer.exe

PySide2库的层级结构

- QtCore 核心算法库
- QtGui 界面图形算法库
- QtWidgets 界面控件库
- uic ui文件到py文件的桥梁
- sip C++对象到Python转换库

QtCore 包含了核心的非GUI的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用。

QtGui 包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类。

QtWidgets类包含了一系列创建桌面应用的UI元素。 QtMultimedia包含了处理多媒体的内容和调用摄像头API的类。 QtBluetooth模块包含了查找和连接蓝牙的类。 QtNetwork包含了网络编程的类，这些工具能让TCP/IP和UDP开发变得更加方便和可靠。 QtPositioning包含了定位的类，可以使用卫星、WiFi甚至文本。 Engine包含了通过客户端进入和管理Qt Cloud的类。 QtWebSockets包含了WebSocket协议的类。 QtWebKit包含了一个基WebKit2的web浏览器。 QtWebKitWidgets包含了基于QtWidgets的WebKit1的类。 QtXml包含了处理xml的类，提供了SAX和DOM API的工具。 QtSvg提供了显示SVG内容的类，Scalable Vector Graphics (SVG)是一种是一种基于可扩展标记语言（XML），用于描述二维矢量图形的图形格式（这句话来自于维基百科）。 QtSql提供了处理数据库的工具。 QtTest提供了测试PyQt5应用的工具。

一般PyQt的代码分手写与Designer设计，Designer设计出来的.ui文件又分两种使用方法，要么编译成.py文件去使用，要么直接通过方法load这个.ui文件来使用。按Python环境来验证哪种更方便。

.. code-block:: python

    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets

    class CustomDialog(QtWidgets.QDialog):
        pass

    if __name__ == "__main__":
        dialog = CustomDialog()
        dialog.show()

.. code-block:: python

    import sys

    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets

    class CustomDialog(QtWidgets.QDialog):
        pass

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        dialog = CustomDialog()
        dialog.show()
        print(dir(app))
        app.exec_()

.. code-block:: python

    import sys

    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets

    class CustomDialog(QtWidgets.QDialog):
        def __init__(self):
            super().__init__()

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        dialog = CustomDialog()
        dialog.show()
        print(dir(app))
        app.exec_()

手写代码

.. code-block:: python

    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets

    class CustomDialog(QtWidgets.QDialog):
        def __init__(self, parent=None):
            # super().__init__(parent)
            super(CustomDialog, self).__init__(parent)

            # mainLayout = QtWidgets.QVBoxLayout()
            # self.setLayout(mainLayout)
            vblLayout = QtWidgets.QVBoxLayout(self)

            gbSim = QtWidgets.QGroupBox()
            gbSim.setTitle("Sim or Seq:")
            hblLayout = QtWidgets.QHBoxLayout(gbSim)
            rbSim = QtWidgets.QRadioButton("Simulation")
            rbSeq = QtWidgets.QRadioButton("Sequence")

            hblLayout.addWidget(rbSim)
            hblLayout.addWidget(rbSeq)

            pbSubmit = QtWidgets.QPushButton("Submit")
            vblLayout.addWidget(gbSim)
            vblLayout.addWidget(pbSubmit)

    if __name__ == "__main__":
        dialog = CustomDialog()
        dialog.show()

PySide2加载.ui文件模式

.. code-block:: python

    from PySide2 import QtUiTools
    from PySide2 import QtWidgets
    from PySide2 import QtGui
    from PySide2 import QtCore

    class CustomDialog(QtWidgets.QDialog):
        def __init__(self, parent=None):
            super(CustomDialog, self).__init__(parent)

            loader = QtUiTools.QUiLoader()

            self.ui = loader.load(r"D:\2020\test.ui")

            mainLayout = QtWidgets.QVBoxLayout()
            mainLayout.setContentsMargins(0, 0, 0, 0)
            mainLayout.addWidget(self.ui)
            self.setLayout(mainLayout)

    dialog = CustomDialog()
    dialog.show()


转py文件

.. code-block:: python

    # C:\Python37\Scripts\pyside2-uic.exe -o D:\2020\mainWin.py D:\2020\test.ui

    import sys

    path = "D:/2020"

    path in sys.path or sys.path.insert(0, path)

    from PySide2 import QtWidgets
    from PySide2 import QtGui
    from PySide2 import QtCore
    import mainWin
    reload(mainWin)

    class CustomDialog(QtWidgets.QDialog, mainWin.Ui_Dialog):
        def __init__(self, parent=None):
            super(CustomDialog, self).__init__(parent)

            self.setupUi(self)

    dialog = CustomDialog()
    dialog.show()

信号与槽（事件）

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

------------------
参考文档
------------------

- https://www.cnblogs.com/jakeyChen/articles/4103494.html
- https://wiki.python.org/moin/PyQt4
- https://www.riverbankcomputing.com/static/Docs/PyQt4/classes.html
- https://doc.qt.io/qtforpython/PySide2/QtWidgets/QPushButton.html
- https://www.riverbankcomputing.com/static/Docs/PyQt4/classes.html
- https://doc.bccnsoft.com/docs/PyQt5/class_reference.html
- https://build-system.fman.io/qt-designer-download
- http://zetcode.com/gui/pyqt4/
