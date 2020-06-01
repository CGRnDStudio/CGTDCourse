=============================
Python流控制语句
=============================

Python流控制语句包括if条件判断语句、for循环语句、while循环语句以及try异常中断语句。

- if条件语句

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

- for循环语句

.. code-block:: python

    # for语句的写法
    for element in iterable:
        statement block

    for element in iterable:
        statement block
    else:
        statement block

break与continue的区别：break中断整个循环语句，continue中断本次循环，继续下一次循环。

- while循环语句

while循环需要注意避免死循环，语句块中需要有自增或自检以结束循环条件。

.. code-block:: python

    # while语句的写法
    while condition:
        statement block

- try异常中断

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

.. code-block:: python

    try:
        1 / 0
    except ZeroDivisionError as e:
        print(e)

异常捕获对于调试代码并不是一件友好的事情，经常在调试代码过程中我们会避免使用try语句以获得代码异常的详细信息。异常也可以自定义，可以通过关键字raise来抛出异常。

.. code-block:: python

    def checkAbs(x):

        if not isinstance(x, (int, float)):
            raise TypeError("x only support int or float")

        if x >= 0:
            return x
        else:
            return -x

不要这样写

.. code-block:: python

    if a == False:
    if a == 0:
    if a == None:
    if a == []:
    if a == "":

建议写成

.. code-block:: python

    if not a:

.. code-block:: python

    userSays = raw_input("请输入:") or "nothing"

    # 三元赋值法
    "hello" if True else "world"
    "hello" if 1 > 2 else "world"

