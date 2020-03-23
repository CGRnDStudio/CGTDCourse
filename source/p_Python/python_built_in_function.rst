=============================
Python内置函数
=============================

Python内置函数也叫内建函数（built-in function），内置函数大约有60来个，都非常有用。

* print()

* len()

* enumerate()

.. code-block:: python

    for i, item in enumerate(myList):
        print(i, "-->", item)

* int() & float() & str() & bool()

* id() & type() & dir() & help()

id() 返回对象的内存地址。
type() 获取对象的类型。
dir() 获取对象的属性和方法。
help() 获取具体属性与方法的帮助文档。

* eval() & exec()

eval() 将一个字符串当成一个表达式来执行，返回表达式执行后的结果。
exec() 将一个字符串当成程序来执行。

* max() & min() & sum()

* abs()

* hex() & oct() & bin()
