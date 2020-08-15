====================================
PyQt自定义控件玩法
====================================

自定义控件，事件机制，如何让UI元素更丰富!

.. code-block:: python

from PySide2 import QtWidgets

    class QLineEditPath(QtWidgets.QLineEdit):

        def __init__(self, parent=None):
            super(QLineEditPath, self).__init__(parent)

        def dragEnterEvent(self, event):

            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()

        def dropEvent(self, event):

            if event.mimeData().hasUrls():
                url = event.mimeData().urls()[0]
                self.setText(url.toLocalFile())

    dialog = QLineEditPath()
    dialog.show()


.. code-block:: python

    from PySide2 import QtCore
    from PySide2 import QtWidgets

    class QLineEditPath(QtWidgets.QLineEdit):

        def __init__(self, parent=None):
            super(QLineEditPath, self).__init__(parent)

        def keyPressEvent(self, event):
            if event.key() == QtCore.Qt.Key_Return:
                self.setText(self.text().replace("\\", "/"))
            else:
                QtWidgets.QLineEdit.keyPressEvent(self, event)

    dialog = QLineEditPath()
    dialog.show()

.. code-block:: python

    class QPublishedFileItem(QtWidgets.QWidget):

        def __init__(self, file_name, file_type, parent=None):
            super(QPublishedFileItem, self).__init__(parent)

            vblFile = QtWidgets.QVBoxLayout()

            lPublishedFileName = QtWidgets.QLabel(file_name)
            lPublishedFileType = QtWidgets.QLabel(file_type)
            # lPublishedFileName = QtWidgets.QLabel("<span style='font-weight: bold;'>lgt_autosphere_02.v007.nk</span> Version 007 (Task lgt_autosphere_02)")
            # lPublishedFileType = QtWidgets.QLabel("<span style='font-size: 10px;'><span style='color: #2e93e2;'>Nuke Script</span> by xu tao at 2020-02-05 17:40</span>")
            vblFile.addWidget(lPublishedFileName)
            vblFile.addWidget(lPublishedFileType)

            hblAction = QtWidgets.QHBoxLayout()
            self.pbAction = QtWidgets.QPushButton("Action")
            self.pbAction.hide()
            self.mAction = QtWidgets.QMenu()
            self.pbAction.setMenu(self.mAction)
            hblAction.addLayout(vblFile)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            hblAction.addItem(spacerItem)
            hblAction.addWidget(self.pbAction)

            vblPublishedFile = QtWidgets.QVBoxLayout()
            # vblPublishedFile.addLayout(vblThumbnail)
            vblPublishedFile.addLayout(hblAction)
            self.setLayout(vblPublishedFile)

    fileName = "<span style='font-weight: bold;'>lgt_autosphere_02.v007.nk</span> Version 007 (Task lgt_autosphere_02)"
    fileType = "<span style='font-size: 10px;'><span style='color: #2e93e2;'>Nuke Script</span> by xu tao at 2020-02-05 17:40</span>"
    dialog = QPublishedFileItem(fileName, fileType)
    dialog.show()
