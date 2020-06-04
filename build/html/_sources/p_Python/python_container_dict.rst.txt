=============================
Python容器：字典 {key: value}
=============================

容器是对专门用来装其它对象的数据类型的统称。在Python中，有四种最常见的内建容器类型：列表（list）、元组（tuple）、字典（dict）和集合（set）。Python语言内部实现细节也与这些容器息息相关。比如Python的类实例属性、全局变量globals()等都是通过字典类型来存储的。

- 字典 dict {key: value}

- 无序的（散列表）

- 可迭代的

字典的迭代本质上并不是字典本身迭代，而是列表的迭代。

.. code-block:: python

    for k, v in dict.items():
    for k in dict.keys():
    for v in dict.values():
    for k, v in dict.iteritems():
    for k in dict.keys():
    for v in dict.values():

- 字典的方法

.. code-block:: python

    >>> type({})
    <type 'dict'>
    >>> dir({})
    ['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
    >>>
