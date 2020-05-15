=============================
Python函数式编程
=============================

函数式编程（Functional Programming，简称FP）理论依据是在Python中一切皆对象

Python函数是一等对象意味着在Python中可以赋值给变量引用。

.. code-block:: python

    >>> def funObject(arg):
    ...     return arg
    ...
    >>> funObject(100)
    100
    >>> funTest = funObject
    >>> funTest
    <function funObject at 0x03239BF0>
    >>> funObject
    <function funObject at 0x03239BF0>
    >>> funTest(99)
    99
    >>>

Python支持高阶函数意味着函数可以接受其它函数作为参数或者返回值。下面有几个经典的案例。

内置函数map()、filter()、reduce()以及sorted()都是高阶函数的经典案例。

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

    >>> help(filter)
    Help on built-in function filter in module __builtin__:

    filter(...)
        filter(function or None, sequence) -> list, tuple, or string

        Return those items of sequence for which function(item) is true.  If
        function is None, return the items that are true.  If sequence is a tuple
        or string, return the same type, else return a list.

    >>> help(reduce)
    Help on built-in function reduce in module __builtin__:

    reduce(...)
        reduce(function, sequence[, initial]) -> value

        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.

    >>> help(sorted)
    Help on built-in function sorted in module __builtin__:

    sorted(...)
        sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

不管是内置函数sorted还是列表方法sort()，都可以传递key参数接受函数来自定义排序方式（通常默认排序方式不满足需求）。

.. code-block:: python

    import re

    files = ["tank_1_color_v0.rat",
             "tank_2_color_v5.rat",
             "tank_1_color_v3.rat",
             "tank_3_color_v1.rat",
             "tank_4_color_v2.rat",
             "tank_4_color_v4.rat",
             "tank_5_color_v1.rat",
             "tank_6_color_v6.rat"]

    pat_num = re.compile("\D+_(\d+)_")
    pat_ver = re.compile("(\d+)\D+$")


    def sorter_num(elem):
        res = re.search(pat_num, elem)
        return res.groups()[0]


    def sorter_ver(elem):
        res = re.search(pat_ver, elem)
        return res.groups()[0]

    print(sorted(files, key=sorter_num))
    print(sorted(files, key=sorter_ver))

    # ['tank_1_color_v0.rat', 'tank_1_color_v3.rat', 'tank_2_color_v5.rat', 'tank_3_color_v1.rat', 'tank_4_color_v2.rat', 'tank_4_color_v4.rat', 'tank_5_color_v1.rat', 'tank_6_color_v6.rat']
    # ['tank_1_color_v0.rat', 'tank_3_color_v1.rat', 'tank_5_color_v1.rat', 'tank_4_color_v2.rat', 'tank_1_color_v3.rat', 'tank_4_color_v4.rat', 'tank_2_color_v5.rat', 'tank_6_color_v6.rat']

因为函数可以作为参数传递，匿名函数应用而生，对于简单的函数可以使用lambda函数一句话来表达。

.. code-block:: python

    import re

    files = ["tank_1_color_v0.rat",
            "tank_2_color_v5.rat",
            "tank_1_color_v3.rat",
            "tank_3_color_v1.rat",
            "tank_4_color_v2.rat",
            "tank_4_color_v4.rat",
            "tank_5_color_v1.rat",
            "tank_6_color_v6.rat"]

    pat_num = re.compile("\D+_(\d+)_")
    pat_ver = re.compile("(\d+)\D+$")

    print(sorted(files, key=lambda elem: re.search(r"\D+_(\d+)_", elem).groups()[0]))
    print(sorted(files, key=lambda elem: re.search(r"(\d+)\D+$", elem).groups()[0]))

    # ['tank_1_color_v0.rat', 'tank_1_color_v3.rat', 'tank_2_color_v5.rat', 'tank_3_color_v1.rat', 'tank_4_color_v2.rat', 'tank_4_color_v4.rat', 'tank_5_color_v1.rat', 'tank_6_color_v6.rat']
    # ['tank_1_color_v0.rat', 'tank_3_color_v1.rat', 'tank_5_color_v1.rat', 'tank_4_color_v2.rat', 'tank_1_color_v3.rat', 'tank_4_color_v4.rat', 'tank_2_color_v5.rat', 'tank_6_color_v6.rat']

Python闭包函数是一种在函数中定义函数的行为，如果将函数以返回值的形式return，是高阶函数的另一种形式。

Python装饰器是闭包函数与高阶函数的一种应用案例。

.. code-block:: python

    import time


    def measure_time(func):

        def wrapped(*args, **kwargs):
            start = time.time()

            try:
                return func(*args, **kwargs)
            finally:
                runtime = time.time() - start
                print "Execution time: %.6f seconds" % runtime

        return wrapped


    @measure_time
    def testFunc(num):
        time.sleep(num)


    testFunc(1)
    testFunc(3)
    testFunc(5)


    # Execution time: 1.000000 seconds
    # Execution time: 3.000000 seconds
    # Execution time: 5.001000 seconds
