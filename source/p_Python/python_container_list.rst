=============================
Python容器：列表 []
=============================

容器是对专门用来装其它对象的数据类型的统称。在Python中，有四种最常见的内建容器类型：列表（list）、元组（tuple）、字典（dict）和集合（set）。Python语言内部实现细节也与这些容器息息相关。比如Python的类实例属性、全局变量globals()等都是通过字典类型来存储的。

* 列表 list []

* 有序的

* 索引取值

* 索引改值

* 切片

* 可变的

* 可迭代的

* 列表的方法

.. code-block:: python

    >>> type([])
    <type 'list'>
    >>> dir([])
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>>

* 列表解包

.. code-block:: python

    >>> a, *b = range(4)
    >>> a
    0
    >>> b
    [1, 2, 3]
    >>>
    >>> a, *b, c = range(4)
    >>> a
    0
    >>> b
    [1, 2]
    >>> c
    3
    >>>

.. code-block:: python

    >>> l = []
    >>> l.append(1)
    >>> print(l)
    [1]
    >>> l.extend([1, 2, 3])
    >>> print(l)
    [1, 1, 2, 3]
    >>> l.count(1)
    2
    >>> l.index(3)
    3
    >>> l.pop()
    3
    >>> print(l)
    [1, 1, 2]
    >>>
    >>> l2 = [1, 2, 3, 4, 5]
    >>> print(l2)
    [1, 2, 3, 4, 5]
    >>> l2.reverse()
    >>> print(l2)
    [5, 4, 3, 2, 1]
    >>> l2.sort()
    >>> print(l2)
    [1, 2, 3, 4, 5]
    >>> l3 = [35, 50, 17, 30]
    >>> print(l3)
    [35, 50, 17, 30]
    >>> sorted(l3)
    [17, 30, 35, 50]
    >>> print(l3)
    [35, 50, 17, 30]
    >>> print(sorted(l3))
    [17, 30, 35, 50]
    >>>

.. code-block:: python

    >>> s1 = set([1, 2, 3, 4, 5])
    >>> s2 = set([3, 5, 7, 8, 9])
    >>> print(s1.union(s2))
    set([1, 2, 3, 4, 5, 7, 8, 9])
    >>> s1 = set(["Andy", "Tommy", "Ben", "Gloria", "Dinna"])
    >>> s2 = set(["John", "Tommy", "Ben", "Gloria", "Dinna"])
    >>> print(s1.difference(s2))
    set(['Andy'])
    >>> d = {"name": "Andy", "age": 28, "country": "China"}
    >>> print(d)
    {'country': 'China', 'age': 28, 'name': 'Andy'}
    >>> print(d["name"])
    Andy
    >>> d["name"] = "Gloria"
    >>> print(d)
    {'country': 'China', 'age': 28, 'name': 'Gloria'}
    >>> d2 = d
    >>> print(d)
    {'country': 'China', 'age': 28, 'name': 'Gloria'}
    >>> print(d2)
    {'country': 'China', 'age': 28, 'name': 'Gloria'}
    >>> d2["name"] = "Andy"
    >>> print(d)
    {'country': 'China', 'age': 28, 'name': 'Andy'}
    >>> print(d2)
    {'country': 'China', 'age': 28, 'name': 'Andy'}
    >>>
    >>> d2 = d.copy()
    >>> print(d)
    {'country': 'China', 'age': 28, 'name': 'Andy'}
    >>> print(d2)
    {'country': 'China', 'age': 28, 'name': 'Andy'}
    >>> d2["name"] = "John"
    >>> print(d)
    {'country': 'China', 'age': 28, 'name': 'Andy'}
    >>> print(d2)
    {'country': 'China', 'age': 28, 'name': 'John'}
    >>> print(id(d))
    58866256
    >>> print(id(d2))
    58867408
    >>> l2 = [9, 5, 45, 2, 1]
    >>> l3 = l2
    >>> print(l2, l3)
    ([9, 5, 45, 2, 1], [9, 5, 45, 2, 1])
    >>> l2.append(100)
    >>> print(l2, l3)
    ([9, 5, 45, 2, 1, 100], [9, 5, 45, 2, 1, 100])
    >>> l4 = l2[:]
    >>> print(l2, l4)
    ([9, 5, 45, 2, 1, 100], [9, 5, 45, 2, 1, 100])
    >>> l2.append(200)
    >>> print(l2, l4)
    ([9, 5, 45, 2, 1, 100, 200], [9, 5, 45, 2, 1, 100])
    >>> print(d2)
    {'country': 'China', 'age': 28, 'name': 'John'}
    >>> print(d2["age"])
    28
    >>> print(d2["ages"])
    >>> print(d2.get("key", None))
    None
    >>> print(d2.has_key("age"))
    True
    >>> print(d2.items())
    [('country', 'China'), ('age', 28), ('name', 'John')]
    >>> print(d2.keys())
    ['country', 'age', 'name']
    >>> print(d2.values())
    ['China', 28, 'John']
    >>> print(d2)
    {'country': 'China', 'age': 28, 'name': 'John'}
    >>> d2.pop("age")
    28
    >>> print(d2)
    {'country': 'China', 'name': 'John'}
    >>> d2.update(dict(age=29))
    >>> print(d2)
    {'country': 'China', 'age': 29, 'name': 'John'}
    >>> range(5, 0, -1)
    [5, 4, 3, 2, 1]
    >>> g = xrange(1000000)
    >>> print(g)
    xrange(1000000)
    >>> print(g[1000])
    1000
    >>>

* 列表推导

.. code-block:: python

    >>> intList = [1, 2, 3]
    >>> print(intList)
    [1, 2, 3]
    >>> intList == [1, 2, "3"]
    False
    >>> print(intList)
    [1, 2, 3]
    >>> print(type(intList))
    <type 'list'>
    >>> nameList = ["andy", "dovfx"]
    >>> print(nameList)
    ['andy', 'dovfx']
    >>> complexList = [99, "hello", [1, 2], nameList]
    >>> print(complexList)
    [99, 'hello', [1, 2], ['andy', 'dovfx']]
    >>> type(complexList)
    <type 'list'>
    >>> print(type(complexList))
    <type 'list'>
    >>> print(range(1, 100))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    >>> print(range(100))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    >>> print(range(1, 100, 5))
    [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
    >>>

.. code-block:: python

    >>> numbers = range(10)
    >>> print(numbers)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> print(numbers[1])
    1
    >>> print(numbers[0])
    0
    >>> print(numbers[-1])
    9
    >>> myList = [numbers, ["a", "b", "c"]]
    >>> print(myList[1][1])
    b
    >>> myList[-1][1] = "bb"
    >>> print(myList)
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ['a', 'bb', 'c']]
    >>> print(numbers[1:7])
    [1, 2, 3, 4, 5, 6]
    >>> print(numbers[3:])
    [3, 4, 5, 6, 7, 8, 9]
    >>> print(numbers[:3])
    [0, 1, 2]
    >>> print(numbers[-4:-1])
    [6, 7, 8]
    >>> print(numbers[3:-2])
    [3, 4, 5, 6, 7]
    >>> print(numbers[1:7:2])
    [1, 3, 5]
    >>> print(dir(numbers))
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>>
    >>> numbers.append(100)
    >>> print(numbers)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
    >>> print(numbers.count(100))
    1
    >>>
    >>> a = ["a", "b", "c"]
    >>> numbers.extend(a)
    >>> print(numbers)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 'a', 'b', 'c']
    >>> numbers = range(10)
    >>> numbers.append(a)
    >>> print(numbers)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ['a', 'b', 'c']]
    >>>
    >>> print(a.index("b"))
    1
    >>> a.append("d")
    >>> a.insert(0, "d")
    >>> a.pop(0)
    'd'
    >>> a.remove("a")
    >>>
    >>> numbers.reverse()
    >>> print(numbers)
    [['b', 'c', 'd'], 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>>
    >>> numbers.sort()
    >>> print(numbers)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ['b', 'c', 'd']]
    >>>

.. code-block:: python

    #!/usr/bin/env python
    import os

    d = dict(spoon=4,
            fork=4,
            plate=7,
            cup=6,
            knife=2,
            teapot=1)

    print d.keys()
    print d.values()
    print d.items()

    # for k,v in d.items():
    #     print k,v
    #
    new_env = {'HOUDINI_PATH': '/mnt/share/repos/hou', 'EDITOR': 'vim', 'TEMP': 'C:/TMP'}
    # for k,v in os.environ.items():
    # 	print k,v


    # os.environ.update(new_env)
    # for k, v in sorted(os.environ.iteritems()):
    #     print k, v

.. code-block:: python

    # -*- coding: UTF-8 -*-

    #NOTE: For more advanced text formating see textwrap module.
    s0 = '           Python 2.6; Python 2.7; Python 3.0; Python 3.3'
    s1 = "Java is a programming language that lets you work more quickly\n" \
        "and integrate your systems more effectively. You can learn to use Java\n" \
        "and see almost immediate gains in productivity and lower maintenance costs"

    s2 = "January February April March May June July August September October November December"

    s3 = "Popular Names : Girls:{Lauren Isabella Ava Lily Zoe Chloe Mia Layla Emily Lucy} " \
        "Boys:{Aiden Jackson Ethan Liam Mason Noah Lucas Jacob Jayden Jack Alexander Ryan}"
    s4 = 'Escape this worlds: \never \try \this'


    print "Lower case :", s0.lower()
    print s0.count('Python')
    print s0.split(';')
    print s0.lstrip()
    print "2.7" in s0
    print s4 #raw string


    # print s1.replace("Java", "Python")
    # print " ??? ".join(s2.split())

    # grlnames = s3[s3.find('Girls:') + len('Girls:') + 1 : s3.find('}')]
    # # print grlnames
    # # print [name for name in grlnames.split(" ") if name.startswith('L')]
    # for name in grlnames.split():
    #      if name.startswith('L'):
    #           print name

.. code-block::python

    ### Format examples
    robot = dict(
        name='Blender',
        numCPU=160,
        version='3.01c',
        memory=64,
        releaseDate=2020
    )

    ############# Old style format ############
    # print "Padding %5d" % 15
    # print "Here is new robot - {name}, it has {numCPU} CPU".format(name = robot['name'],numCPU = robot['numCPU'])
    # print robot


    # print "Here is new robot - {0}, it has {1} CPU's, {2}GB of memory,\n"\
    #        "OS Version: {3}. It will be available in year {4}".format(*robot.values()) ## New in python 2.6

    # ## Floating point precision
    print "Round number {0:.3}".format(5.00000009)
    print "{0:,.03f}".format(1500000)
    print "Zero padding: {0:04}".format(19)

    # ## Thousands separator
    # print "{0:,}".format(100500133)

    ## Fill with character
    # print "{0:#^30}\n{1:.^30}".format('','HELLO')

    ### Print multiplication result
    # def nice_print():
    #     result = ''
    #     for x in range(1, 11):
    #         result += '{0}){0:.> 10}*{0} = {1}\n'.format(x, x * x)
    #     print result

    # nice_print()
