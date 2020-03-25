=============================
Python数据类型：整型 & 浮点型
=============================

------------------
整型
------------------

小整数缓存池：[-5, 257)

算术运算符

.. code-block:: bash

    +, -, *, /, %, //

.. code-block:: bash

    >>> 1 + 2
    3
    >>> 1.0 + 2
    3.0
    >>> 10 / 3
    3
    >>> 10 / 3.0
    3.3333333333333335
    >>> 10.0 // 3.3
    3.0
    >>> 1.1 % 0.3
    0.20000000000000012
    >>> "hello " + "world"
    'hello world'
    >>> "hello" * 5
    'hellohellohellohellohello'
    >>> True + True
    2
    >>> 5 / False
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero
    >>>
