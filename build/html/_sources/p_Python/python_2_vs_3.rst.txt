=============================
Python 2.x VS 3.x
=============================

* 3.x版本中取消print空格打印的写法，只能用print()内置函数

.. code-block:: bash

    # 2.x
    >>> print 100
    100
    >>>

* 3.x版本中新的解包写法，2.x中会语法异常

.. code-block:: bash

    # 3.x
    >>> a, *b = [1, 2, 3, 4]
    >>> a
    1
    >>> b
    [2, 3, 4]
    >>>

* 3.x版本中取消xrange()写法，range()返回生成器

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

