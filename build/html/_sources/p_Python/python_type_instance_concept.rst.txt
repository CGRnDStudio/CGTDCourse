=============================
Python类型实例概念
=============================

Python中万物皆对象，但是得先有类型，才能生成实例对象。我们操作某一个实例的时候，首先得分析它是什么类型，可以通过type()来获取对象的类型，然后分析它有什么属性以及方法，可以通过dir()来获取对象的属性和方法，再然后可以通过help()来获取具体属性与方法的帮助文档。

.. code-block:: python

    >>> s1 = "Hello world!"
    >>> s1
    'Hello world!'
    >>> type(s1)
    <type 'str'>
    >>> dir(s1)
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    >>> help(s1.split)
    Help on built-in function split:

    split(...)
        S.split([sep [,maxsplit]]) -> list of strings

        Return a list of the words in the string S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are removed
        from the result.
    >>> s1.split()
    ['Hello', 'world!']

可以看出type()、dir()以及help()乃是一套通用心法，无论你得到一个什么实例对象，你都可以通过此三个内置函数来获取对于这个对象的初步的文档以及使用方法。
