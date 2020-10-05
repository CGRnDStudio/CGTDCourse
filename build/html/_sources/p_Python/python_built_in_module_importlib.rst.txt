=============================
Python内置模块：importlib
=============================

importlib是Python 3加入的模块，里面有个重要的方法reload在Python 2中是内置函数。

.. code-block:: python

    >>> import importlib
    >>> importlib.__file__
    'C:\\Python37\\lib\\importlib\\__init__.py'
    >>> dir(importlib)
    ['_RELOADING', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__import__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_bootstrap', '_bootstrap_external', '_imp', '_r_long', '_w_long', 'abc', 'find_loader', 'import_module', 'invalidate_caches', 'machinery', 'reload', 'sys', 'types', 'util', 'warnings']
    >>>
    >>> import os
    >>> importlib.reload(os)
    <module 'os' from 'C:\\Python37\\lib\\os.py'>
    >>>