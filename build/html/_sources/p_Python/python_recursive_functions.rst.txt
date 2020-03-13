===============
Python递归函数
===============

所谓递归就是在函数内部调用自己的函数被称之为递归。

------------------
坐井观天: 知识体系
------------------

阶乘函数 ``n!``

.. code-block:: python

    def fact(n):

        if n == 1:
            return 1
        
        return n * fact(n - 1)

斐波那契数列 ``1, 1, 2, 3, 5, 8...``

.. code-block:: python

    def fib(n):

        if n < 2:
            return n

        return fib(n - 1) + fib(n - 2)


------------------
管中窥豹: 延伸阅读
------------------


