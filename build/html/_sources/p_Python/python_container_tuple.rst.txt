=============================
Python容器：元组 ()
=============================

容器是对专门用来装其它对象的数据类型的统称。在Python中，有四种最常见的内建容器类型：列表（list）、元组（tuple）、字典（dict）和集合（set）。Python语言内部实现细节也与这些容器息息相关。比如Python的类实例属性、全局变量globals()等都是通过字典类型来存储的。

- 元组 tuple ()

- 不可变的

元组的不可变是相对的。

- 有序的

- 索引 & 切片

- 可迭代的

- 元组的方法

.. code-block:: python

    >>> type(())
    <type 'tuple'>
    >>> dir(())
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
    >>>
