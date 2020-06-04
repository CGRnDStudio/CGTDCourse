=============================
Python匿名函数
=============================

匿名函数并不是说函数没有名字，而是def自定义函数如果简单到只用一句表达式就可以描述的时候，就可以使用lambda关键字来替代。

lambda函数基本语法规则:

.. code-block:: python

    lambda arguments: expression

lambda函数也支持缺省参数、可变参数以及关键字参数，和def自定义函数参数规则完全相同。

.. code-block:: python

    >>> add = lambda x, y=0: x + y
    >>> add(100, 200)
    300
    >>> add(100)
    100

Python函数式编程很容易涉及到匿名函数，高阶函数一般接收函数对象作为参数，而lambda表达式在合适不过。

.. code-block:: python

    >>> help(map)
    Help on built-in function map in module __builtin__:

    map(...)
        map(function, sequence[, sequence, ...]) -> list

        Return a list of the results of applying the function to the items of
        the argument sequence(s).  If more than one sequence is given, the
        function is called with an argument list consisting of the corresponding
        item of each sequence, substituting None for missing values when not all
        sequences have the same length.  If the function is None, return a list of
        the items of the sequence (or a list of tuples if more than one sequence).

    >>>
    >>> map(lambda x: x % 2 or x, range(10))
    [0, 1, 2, 1, 4, 1, 6, 1, 8, 1]
    >>>
    >>> help(filter)
    Help on built-in function filter in module __builtin__:

    filter(...)
        filter(function or None, sequence) -> list, tuple, or string

        Return those items of sequence for which function(item) is true.  If
        function is None, return the items that are true.  If sequence is a tuple
        or string, return the same type, else return a list.
    >>>
    >>> filter(lambda x: not x % 2, range(10))
    [0, 2, 4, 6, 8]
    >>>

lambda函数中如何使用if, else以及elif?

在lambda函数中使用if else有点棘手，基本语法规则:

.. code-block:: python

    lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>

比如我们创建一个lambda函数来检查给定值是否在-5到5之间，可以这样:

.. code-block:: python

    >>> filterFunc = lambda x: True if (x > -5 and x < 5) else False
    >>> filterFunc(-2)
    True
    >>> filterFunc(5)
    False
    >>> filterFunc(10)
    False
    >>>

在这里，我们在lambda函数中使用if else，如果给定值在-5到5之间，则它将返回True，否则它将返回False。

实际在lambda函数中，我们可以避免使用if else的写法，下面是更pythonic的写法，仍然可以获得相同的结果。

.. code-block:: python

    >>> filterFunc = lambda x: x > -5 and x < 5
    >>>
    >>> filterFunc(-2)
    True
    >>> filterFunc(5)
    False
    >>> filterFunc(10)
    False
    >>>

高阶函数filter和lambda函数一起使用会发生微妙的变化，filter高阶函数接受callback函数，内置循环遍历每一个元素，如果callback函数返回True，则将元素添加到新列表。

.. code-block:: python

    >>> help(filter)
    Help on built-in function filter in module __builtin__:

    filter(...)
        filter(function or None, sequence) -> list, tuple, or string

        Return those items of sequence for which function(item) is true.  If
        function is None, return the items that are true.  If sequence is a tuple
        or string, return the same type, else return a list.
    >>>
    >>> filter(lambda x: not x % 2, range(10))
    [0, 2, 4, 6, 8]
    >>>

那么如果多个条件如何在lambda函数中使用if, elif和else呢?

我们不能在lambda函数中直接使用elif，可以使用if else加括号的方式。基本语法规则:

.. code-block:: python

    lambda <args> : <return Value> if <condition> (<return value> if <condition> else <return value>)

.. code-block:: python

    >>> converter = lambda x: x * 2 if x < 10 else (x * 3 if x < 20 else x)
    >>> converter(5)
    10
    >>> converter(13)
    39
    >>> converter(23)
    23
    >>>

sort排序使用

re正则替换使用
