====================================
PyQt实现Maya中frameLayout布局功能
====================================

.. code-block:: python

    import maya.cmds as cmds

    cmds.window()
    cmds.scrollLayout( 'scrollLayout' )
    cmds.columnLayout( adjustableColumn=True )
    cmds.frameLayout( label='Buttons', collapsable=1)
    cmds.columnLayout()
    cmds.button()
    cmds.button()
    cmds.button()
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.frameLayout( label='Scroll Bars', collapsable=1)
    cmds.columnLayout()
    cmds.intSlider()
    cmds.intSlider()
    cmds.intSlider()
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.frameLayout( label='Fields', collapsable=1)
    cmds.columnLayout()
    cmds.intField()
    cmds.intField()
    cmds.intField()
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.frameLayout( label='Check Boxes', collapsable=1)
    cmds.columnLayout()
    cmds.checkBox()
    cmds.checkBox()
    cmds.checkBox()
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.showWindow()

.. code-block:: python

    from PySide import QtCore
    from PySide import QtGui

    class FrameWidget(QtGui.QGroupBox):
        def __init__(self, title='', parent=None):
            super(FrameWidget, self).__init__(title, parent)
            
            layout = QtGui.QVBoxLayout()
            layout.setContentsMargins(0, 7, 0, 0)
            layout.setSpacing(0)
            super(FrameWidget, self).setLayout(layout)
            
            self.__widget = QtGui.QFrame(parent)
            self.__widget.setFrameShape(QtGui.QFrame.Panel)
            self.__widget.setFrameShadow(QtGui.QFrame.Plain)
            self.__widget.setLineWidth(0)
            layout.addWidget(self.__widget)
            
            self.__collapsed = False
        
        def setLayout(self, layout):
            self.__widget.setLayout(layout)
            
        def expandCollapseRect(self):
            return QtCore.QRect(0, 0, self.width(), 20)

        def mouseReleaseEvent(self, event):
            if self.expandCollapseRect().contains(event.pos()):
                self.toggleCollapsed()
                event.accept()
            else:
                event.ignore()
        
        def toggleCollapsed(self):
            self.setCollapsed(not self.__collapsed)
            
        def setCollapsed(self, state=True):
            self.__collapsed = state

            if state:
                self.setMinimumHeight(20)
                self.setMaximumHeight(20)
                self.__widget.setVisible(False)
            else:
                self.setMinimumHeight(0)
                self.setMaximumHeight(1000000)
                self.__widget.setVisible(True)
        
        def paintEvent(self, event):
            painter = QtGui.QPainter()
            painter.begin(self)
            
            font = painter.font()
            font.setBold(True)
            painter.setFont(font)

            x = self.rect().x()
            y = self.rect().y()
            w = self.rect().width()
            offset = 25
            
            painter.setRenderHint(painter.Antialiasing)
            painter.fillRect(self.expandCollapseRect(), QtGui.QColor(93, 93, 93))
            painter.drawText(
                x + offset, y + 3, w, 16,
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop,
                self.title()
                )
            self.__drawTriangle(painter, x, y)#(1)
            painter.setRenderHint(QtGui.QPainter.Antialiasing, False)
            painter.end()
            
        def __drawTriangle(self, painter, x, y):#(2)        
            if not self.__collapsed:#(3)
                points = [  QtCore.QPoint(x+10,  y+6 ),
                            QtCore.QPoint(x+20, y+6 ),
                            QtCore.QPoint(x+15, y+11)
                            ]
                
            else:
                points = [  QtCore.QPoint(x+10, y+4 ),
                            QtCore.QPoint(x+15, y+9 ),
                            QtCore.QPoint(x+10, y+14)
                            ]
                
            currentBrush = painter.brush()#(4)
            currentPen   = painter.pen()
            
            painter.setBrush(
                QtGui.QBrush(
                    QtGui.QColor(187, 187, 187),
                    QtCore.Qt.SolidPattern
                    )
                )#(5)
            painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))#(6)
            painter.drawPolygon(QtGui.QPolygon(points))#(7)
            painter.setBrush(currentBrush)#(8)
            painter.setPen(currentPen)

    window = QtGui.QMainWindow()
    window.setWindowTitle('Frame Widget Test')

    frame = FrameWidget('Frame Title', window)
    window.setCentralWidget(frame)

    widget = QtGui.QWidget(frame)
    layout = QtGui.QVBoxLayout(widget)
    frame.setLayout(layout)
    for i in range(5):
        layout.addWidget(QtGui.QPushButton('Button %s' % i, widget))

    window.show()

.. code-block:: python

    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets

    class FrameWidget(QtWidgets.QGroupBox):
        def __init__(self, title='', parent=None):
            super(FrameWidget, self).__init__(title, parent)

            layout = QtWidgets.QVBoxLayout()
            layout.setContentsMargins(0, 7, 0, 0)
            layout.setSpacing(0)
            super(FrameWidget, self).setLayout(layout)

            self.__widget = QtWidgets.QFrame(parent)
            self.__widget.setFrameShape(QtWidgets.QFrame.Panel)
            self.__widget.setFrameShadow(QtWidgets.QFrame.Plain)
            self.__widget.setLineWidth(0)
            layout.addWidget(self.__widget)

            self.__collapsed = False

        def setLayout(self, layout):
            self.__widget.setLayout(layout)

        def expandCollapseRect(self):
            return QtCore.QRect(0, 0, self.width(), 20)

        def mouseReleaseEvent(self, event):
            if self.expandCollapseRect().contains(event.pos()):
                self.toggleCollapsed()
                event.accept()
            else:
                event.ignore()

        def toggleCollapsed(self):
            self.setCollapsed(not self.__collapsed)

        def setCollapsed(self, state=True):
            self.__collapsed = state

            if state:
                self.setMinimumHeight(20)
                self.setMaximumHeight(20)
                self.__widget.setVisible(False)
            else:
                self.setMinimumHeight(0)
                self.setMaximumHeight(1000000)
                self.__widget.setVisible(True)

        def paintEvent(self, event):
            painter = QtGui.QPainter()
            painter.begin(self)

            font = painter.font()
            font.setBold(True)
            painter.setFont(font)

            x = self.rect().x()
            y = self.rect().y()
            w = self.rect().width()
            offset = 25

            painter.setRenderHint(painter.Antialiasing)
            painter.fillRect(self.expandCollapseRect(), QtGui.QColor(93, 93, 93))
            painter.drawText(
                x + offset, y + 3, w, 16,
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop,
                self.title()
                )
            self.__drawTriangle(painter, x, y)#(1)
            painter.setRenderHint(QtGui.QPainter.Antialiasing, False)
            painter.end()

        def __drawTriangle(self, painter, x, y):#(2)        
            if not self.__collapsed:#(3)
                points = [  QtCore.QPoint(x+10,  y+6 ),
                            QtCore.QPoint(x+20, y+6 ),
                            QtCore.QPoint(x+15, y+11)
                            ]

            else:
                points = [  QtCore.QPoint(x+10, y+4 ),
                            QtCore.QPoint(x+15, y+9 ),
                            QtCore.QPoint(x+10, y+14)
                            ]

            currentBrush = painter.brush()#(4)
            currentPen = painter.pen()

            painter.setBrush(
                QtGui.QBrush(
                    QtGui.QColor(187, 187, 187),
                    QtCore.Qt.SolidPattern
                    )
                )#(5)
            painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))#(6)
            painter.drawPolygon(QtGui.QPolygon(points))#(7)
            painter.setBrush(currentBrush)#(8)
            painter.setPen(currentPen)

    window = QtWidgets.QMainWindow()
    window.setWindowTitle('Frame Widget Test')

    frame = FrameWidget('Frame Title', window)
    window.setCentralWidget(frame)

    widget = QtWidgets.QWidget(frame)
    layout = QtWidgets.QVBoxLayout(widget)
    frame.setLayout(layout)
    for i in range(5):
        layout.addWidget(QtWidgets.QPushButton('Button %s' % i, widget))

    window.show()

- https://kiwamiden.com/make-mayas-framelayout-with-pyside
