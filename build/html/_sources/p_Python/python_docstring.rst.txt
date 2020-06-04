=============================
Python注释文档
=============================

- docstring

单行代码注释
多行代码注释


docstring规范
都是以三引号的字符串
自定义模块在开始
自定义函数def之后
自定义class之后

.. code-block:: python

    def sceneViewer():
        """ Returns an existing open Scene Viewer pane if there is one. A
            Context viewer is also acceptable is no dedicated scene viewer
            is found.
        """

如何将docstring转成html文档？
