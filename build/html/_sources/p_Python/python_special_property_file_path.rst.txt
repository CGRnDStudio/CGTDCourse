=======================================
Python特殊属性：__file__ & __path__
=======================================

__file__是模块对象的特殊属性，它会返回模块文件的完整路径，如果模块是包的话，则返回包的__init__.py的完整路径。这在工作中非常实用，比如我自定义了一个命名污染的模块platform.py，在使用的时候一直报错，就可以通过代码查找此模块的路径，就会发现系统已经存在这个模块，是因为导入的不是我写的这个模块导致的错误，很多时候很方便检查代码在什么地方。

.. code-block:: python

    >>> import platform
    >>> platform.__file__
    'C:\\Python27\\lib\\platform.pyc'

__path__是模块包的特殊属性，它会返回模块包的文件夹完整路径。

.. code-block:: python

    >>> import PySide
    >>> PySide.__file__
    'C:\\Python27\\lib\\site-packages\\PySide\\__init__.pyc'
    >>> PySide.__path__
    ['C:\\Python27\\lib\\site-packages\\PySide']
