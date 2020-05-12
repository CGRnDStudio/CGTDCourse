=============================
PyQt富文本
=============================

创建QLabel控件，如何让文本丰富起来，比如将其中一部分字体设置为红色该如何操作？

打开Nuke Script Editor或者Maya Script Editor验证下面的代码。

.. code-block:: python

    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets


    widget = QtWidgets.QLabel("<span style='color: red;'>Hello</span> World")
    widget.show()

.. code-block:: python

    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets


    widget = QtWidgets.QLabel("<span style='color: red;'>Hello</span><br> World")
    widget.show()

==================== ================================================
红色                   <span style='color: red;'>text</span>
绿色                   <span style='color: green;'>text</span>
蓝色                   <span style='color: blue;'>text</span>
颜色                   <span style='color: #2e93e2;'>text</span>
加粗                   <span style='font-weight: bold;'>text</span>
字体大小               <span style='font-size: 10px;'>text</span>
换行                   <br>
下划线                 <u>text</u>
斜体                   <i>text</i>
加粗                   <b>text</b>
删除线                 <s>text</s>
==================== ================================================

--------------------
参考文档
--------------------

- https://doc.qt.io/qtforpython/overviews/examples-richtext.html
- https://blog.csdn.net/humanking7/article/details/80685893
