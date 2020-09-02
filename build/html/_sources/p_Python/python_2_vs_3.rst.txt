=============================
Python 2.x VS 3.x
=============================

- 3.x版本中取消print空格打印的写法，只能用内置函数print()

.. code-block:: bash

    # 2.x
    >>> print 100
    100
    >>>

- 3.x版本中新的解包写法，2.x中会语法异常

.. code-block:: bash

    # 3.x
    >>> a, *b = [1, 2, 3, 4]
    >>> a
    1
    >>> b
    [2, 3, 4]
    >>>

- 3.x版本中默认使用utf-8编码，下面的写法在3.x中是合法的，但禁止使用

.. code-block:: bash

    # 3.x
    >>> 变量 = 100
    >>> 变量
    100
    >>>

- 3.x版本中取消xrange()写法，range()返回生成器

.. code-block:: bash

    # 2.x
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> xrange(10)
    xrange(10)
    >>> type(xrange(10))
    <type 'xrange'>
    >>>

    # 3.x
    >>> range(10)
    range(0, 10)
    >>> xrange(10)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'xrange' is not defined
    >>> type(range(10))
    <class 'range'>
    >>>

- 3.x版本中除法的精度变浮点数

.. code-block:: bash

    # 3.x
    >>> 1 / 2
    0.5
    >>>

- 3.x版本中map，filter从内置函数变成了类，得到的结果是迭代对象

.. code-block:: bash

    # 3.x
    >>> map
    <class 'map'>
    >>> filter
    <class 'filter'>

- 3.x版本中reduce从内置函数挪到functools模块中

.. code-block:: bash

    # 3.x
    >>> from functools import reduce
    >>> reduce
    <built-in function reduce>
    >>>

- 3.x版本中没有保留raw_input()，使用input()，在2.x版本中raw_input()将所有输入作为字符串看待，返回字符串类型，input()接收实例对象的输入，在3.x中input()接收任意输入，将所有输入默认当字符串处理，并返回字符串类型。

.. code-block:: bash

    # 3.x
    >>> var = input("Enter something:")
    Enter something:10
    >>> type(var)
    <class 'str'>
    >>> var = input("Enter something:")
    Enter something:andy
    >>> type(var)
    <class 'str'>
    >>>

- 3.x版本中字典方法去掉了has_key()、iteritems()、iterkeys()、itervalues()、viewitems()、viewkeys()和viewvalues()，其中items()、keys()、values()返回迭代器

.. code-block:: bash

    # 3.x
    >>> dir(dict())
    ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
    >>>
    # 2.x
    >>> dir(dict())
    ['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
    >>>

- 3.x版本中去掉了<>不等于的写法，统一用!=

.. code-block:: bash

    # 2.x
    >>> 100 <> 200
    True
    >>>

- 3.x版本中添加海象运算符

- 3.x版本中添加F-Strings格式化字符串方法

- 3.x版本中将reload加入到importlib模块中，不能直接使用

