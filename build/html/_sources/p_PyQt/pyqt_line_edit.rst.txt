=============================
PyQt重写QLineEdit支持拖拽功能
=============================

.. code-block:: python

    class QLineEditPath(QtGui.QLineEdit):

        def __init__(self, parent):
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
