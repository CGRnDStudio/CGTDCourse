=============================
Python内置模块：pprint
=============================

.. code-block:: python

    >>> import pprint
    >>> type(pprint)
    <class 'module'>
    >>> dir(pprint)
    ['PrettyPrinter', '_StringIO', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_builtin_scalars', '_collections', '_perfcheck', '_recursion', '_safe_key', '_safe_repr', '_safe_tuple', '_sys', '_types', '_wrap_bytes_repr', 'isreadable', 'isrecursive', 'pformat', 'pp', 'pprint', 're', 'saferepr']
    >>> pprint.__file__
    'C:\\Python38\\lib\\pprint.py'
    >>> import sys
    >>> pprint.pprint(sys.path)
    ['',
    'C:\\Python38\\python38.zip',
    'C:\\Python38\\DLLs',
    'C:\\Python38\\lib',
    'C:\\Python38',
    'C:\\Python38\\lib\\site-packages']
    >>>
