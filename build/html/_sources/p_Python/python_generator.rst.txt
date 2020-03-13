===============
Python生成器
===============

生成器的本质也是迭代器，惰性迭代，在于减少内存占用。

------------------
坐井观天: 知识体系
------------------

yield与return的区别

next()与__next__()

.. code-block:: python

    def generatorFunc():
        a = 1
        yield a

        a = 2
        yield a

        a = 3
        yield a


------------------
管中窥豹: 延伸阅读
------------------
