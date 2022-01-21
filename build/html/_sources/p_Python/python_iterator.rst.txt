=============================
Python迭代器
=============================

- 迭代器对象
- 可迭代对象

.. code-block:: python

    from collections import Iterator
    from collections import Iterable

    print(help(Iterator))
    print(help(Iterable))


.. code-block:: python

    list1 = range(5)
    iter1 = iter(list1)
    print(list1.__next__)
    print(type(list1))
    print(type(iter1))


