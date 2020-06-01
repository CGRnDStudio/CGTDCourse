=============================
Python数据类型：整型 & 浮点型
=============================

整型即整数（int），Python在内存中有一个小整数缓存池：[-5, 257)。

浮点型也称浮点数，即小数，在内存中存储的精度比整型要高。

.. code-block:: python

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

.. code-block:: python

    >>> a = 5
    >>> a
    5
    >>> a = 3.3
    >>> a
    3.3
    >>> a = "andy"
    >>> a
    'andy'
    >>> a = True
    >>> a
    True
    >>> b = False
    >>> b
    False
    >>> a == b
    False
    >>> a != b
    True
    >>> s = "My Name is Andy"
    >>> s2 = "Hello "
    >>> s2 + s
    'Hello My Name is Andy'
    >>> s - "Name"
    >>> dir(s)
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    >>>
    >>>
    >>> s.capitalize()
    'My name is andy'
    >>> s.upper()
    'MY NAME IS ANDY'
    >>> s.endswith("y")
    True
    >>> s.find("n")
    12
    >>> "My name is %s" % "Andy"
    'My name is Andy'
    >>> "My name is {0}".format("Andy")
    'My name is Andy'
    >>> "My name is {0}, age is {1}".format("Andy", 28)
    'My name is Andy, age is 28'
    >>> "My name is %s, age is %d".format("Andy", 28)
    'My name is %s, age is %d'
    >>> "My name is %s, age is %d" % ("Andy", 28)
    'My name is Andy, age is 28'
    >>>
    >>> print("流浪地球")
    流浪地球
    >>> print(u"流浪地球")
    脕梅脌脣碌脴脟貌
    >>> print("My name is Andy.\nMy age is 28.")
    My name is Andy.
    My age is 28.
    >>> print(r"My name is Andy.\nMy age is 28.")
    My name is Andy.\nMy age is 28.
    >>> s3 = "Hello Andy  "
    >>> s3
    'Hello Andy  '
    >>> s3.strip()
    'Hello Andy'
    >>> s4 = "Name1 Name2 Name3"
    >>> s4.split()
    ['Name1', 'Name2', 'Name3']
    >>> s4.startswith("N")
    True
    >>>
    >>> print("hello world")
    hello world
    >>> print("123")
    123
    >>> print(123)
    123
    >>> print("how are you?")
    how are you?
    >>> print("I'm OK!")
    I'm OK!
    >>> print("""
    ... this is a multi-line string.
    ... it has two lines.
    ... """)

    this is a multi-line string.
    it has two lines.

    >>> print('''
    ... this is a multi-line string.
    ... it has two lines.
    ... ''')

    this is a multi-line string.
    it has two lines.

    >>>
    >>> print(1 + 2)
    3
    >>> print(1.0 + 2)
    3.0
    >>> print(10 / 3)
    3
    >>> print(10 / 3.0)
    3.33333333333
    >>> print(10.0 / 3.3)
    3.0303030303
    >>> print(10.0 // 3.3)
    3.0
    >>> print(10 / 3)
    3
    >>> print(1.1 % 0.3)
    0.2
    >>> print("hello" + "world")
    helloworld
    >>> print("hello" * 5)
    hellohellohellohellohello
    >>> print(True + True)
    2
    >>>
    >>> print(3  > 4)
    False
    >>> print(4 < 5)
    True
    >>> print(5 == 6)
    False
    >>> print(5 is 5)
    True
    >>>
