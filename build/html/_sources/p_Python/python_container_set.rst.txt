=============================
Python容器：集合 {}
=============================

容器是对专门用来装其它对象的数据类型的统称。在Python中，有四种最常见的内建容器类型：列表（list）、元组（tuple）、字典（dict）和集合（set）。Python语言内部实现细节也与这些容器息息相关。比如Python的类实例属性、全局变量globals()等都是通过字典类型来存储的。

- 集合 set {}

集合与字典都是使用花括号{}来定义，区别是字典是通过键值对的方式存储。

- 元素唯一性

- 集合方法

.. code-block:: python

    >>> type(set())
    <type 'set'>
    >>> dir(set())
    ['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
    >>>