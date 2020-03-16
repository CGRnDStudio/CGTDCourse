=============================
Python流控制语句
=============================

Python流控制语句包括if条件判断语句、for循环语句、while循环语句以及try异常中断语句。

--------------
if条件判断语句
--------------

if语句如果条件太多，可以使用字典替代方案。

.. code-block:: python

    # if语句的几种常见写法
    if condition:
        statement block

    if condition:
        statement block
    else:
        statement block

    if condition:
        statement block
    elif condition:
        statement block
    ...
    else:
        statement block

--------------
for循环语句
--------------

.. code-block:: python

    # for语句的写法
    for element in iterable:
        statement block

    for element in iterable:
        statement block
    else:
        statement block

break与continue的区别

* break中断整个循环语句
* continue中断本次循环，继续下一次循环

--------------
while循环语句
--------------

while循环需要注意避免死循环，语句块中需要有自增或自检以结束循环条件。

.. code-block:: python

    # while语句的写法
    while condition:
        statement block

---------------
try异常中断语句
---------------

.. code-block:: python

    # try语句的写法

    try:
        statement block
    except:
        statement block

    try:
        statement block
    except A:
        statement block
    except B:
        statement block
    except:
        statement block
    else:
        statement block
    finally:
        statement block