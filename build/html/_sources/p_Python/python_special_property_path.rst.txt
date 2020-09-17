=============================
Python特殊属性：__path__
=============================

__path__是模块包的特殊属性，它会返回模块包的文件夹完整路径。

.. code-block:: python

    >>> import PySide
    >>> PySide.__file__
    'C:\\Python27\\lib\\site-packages\\PySide\\__init__.pyc'
    >>> PySide.__path__
    ['C:\\Python27\\lib\\site-packages\\PySide']
