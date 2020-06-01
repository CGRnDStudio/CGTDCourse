=============================
Python数据类型：字符串
=============================

字符串（str）是编程语言中最基本也是最重要的一种数据类型，在Python中可以说无时无刻不会跟字符串打交道。

- 字符串定义

三引号正常用于多行注释Docstring。

.. code-block:: python

    "andy"
    'andy'
    """andy"""
    '''andy'''

- 字符串格式化

    - %
    - .format()
    - F-Strings
    - format()

- 字符串索引取值

- 字符串不可变性

- 字符串切片

- 字符串循环迭代

- 字符串方法

掌握字符串方法是非常重要的一项技能，特别是常用的format、join、split和replace四个方法。

.. code-block:: python

    >>> type("python")
    <type 'str'>
    >>>
    >>> dir("python")
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    >>>

- 转义字符

    - \n
    - %%
    - \\

- 字符编码

    - ASCII
    - GB2312
    - GBK
    - Unicode
    - UTF-8