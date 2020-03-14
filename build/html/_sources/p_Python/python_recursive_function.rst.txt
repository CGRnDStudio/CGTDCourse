=============================
Python递归函数
=============================

所谓递归就是在函数内部调用自己的函数被称之为递归，一般递归函数都有终止条件，采用的是后入先出的压栈数据结构。

------------------
坐井观天: 知识体系
------------------

阶乘函数 ``n!``

.. code-block:: python

    def factorial(n):

        if n == 1:
            return 1
        
        return n * factorial(n - 1)

斐波那契数列 ``1, 1, 2, 3, 5, 8...``

.. code-block:: python

    def fibonacci(n):

        if n < 2:
            return n

        return fibonacci(n - 2) + fibonacci(n - 1)


------------------
管中窥豹: 延伸阅读
------------------

从递归函数谈
os.walk()
os.listdir()
os.mkdir()
os.makedirs()
os.rmdir()
os.removedirs()
copy.copy()
copy.deepcopy()
深浅拷贝

从递归函数谈reduce

