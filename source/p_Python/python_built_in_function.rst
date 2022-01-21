=============================
Python内置函数
=============================

Python内置函数也叫内建函数（built-in function），大概有60来个内置函数，版本不同个数不同，功能也有所更新，具体Python环境具体分析（以下内置函数是基于Python 3.8版本）。

.. code-block:: python

    import __builtin__
    print(dir(__builtin__))

=============== ===============================================================
  abs()         # 求绝对值
  all()         # 容器中所有元素都为真返回True，否则返回False
  any()         # 容器中所有元素都为假返回False，否则返回True
  ascii()       # 是ascii码中元素返回该值，不是返回u""
  bin()         # 二进制强制类型转换
  bool()        # 布尔类型强制类型转换，用来测试一个对象的真假状态
  breakpoint()  # 
  bytearray()   # 返回一个新字节数组
  bytes()       # 将字符串转化成bytes类型
  callable()    # 判断对象是否可调用
  chr()         # ASCII编码转字符
  classmethod() # 类相关
  compile()     # 将字符串类型代码编码
  complex()     # 返回一个复数
=============== ===============================================================

.. code-block:: python

    >>> abs(-100)
    100
    >>>

.. code-block:: python

    for i, item in enumerate(range(10, 20, 2)):
        print(i, "-->", item)

=============== ===============================================================
  delattr()     # 类相关
  dict()        # 字典容器强制转换
  dir()         # 返回对象的属性和方法
  divmod()      # 返回商和余数
  enumerate()   # 索引遍历
  eval()        # 将一个字符串当成一个表达式来执行，返回表达式执行后的结果。
  exec()        # 将一个字符串当成程序来执行。
  filter()      # 高阶函数，将容器中元素通过函数过滤成新的容器
  float()       # 浮点型强制类型转换
  format()      # 字符串格式化函数，通常都使用字符串方法或者%的格式化
  frozenset()   # 转换为不可变集合
  getattr()     # 类相关
  globals()     # 返回全局作用域中的名称空间
  hasattr()     # 类相关
=============== ===============================================================

.. code-block:: python

    filter(bool, [1, 0, 2, "", [], 3])

.. code-block:: python

    >>> format(1/2.43, "0.4f")
    '0.4115'
    >>> "{:0.4f}".format(1/2.43)
    '0.4115'
    >>>

=============== ===============================================================
  hash()        # 获取对象的哈希值
  help()        # 获取对象具体属性或方法的帮助文档
  hex()         # 十六进制强制类型转换
  id()          # 返回对象的内存地址
  input()       # 标准输入
  int()         # 整型强制类型转换
  isinstance()  # 判断对象是否是某一类型
  issubclass()  # 类相关
  iter()        # 迭代器函数
  len()         # 返回容器元素个数
  list()        # 将一个可迭代对象转换成列表
  locals()      # 返回当前作用域中的名称空间
  map()         # 高阶函数，将容器中元素通过函数映射成新的容器
  max()         # 返回容器中最大元素
=============== ===============================================================

.. code-block:: python

    >>> iter(range(3))
    <listiterator object at 0x031A03F0>
    >>> iterator = iter(range(3))
    >>> next(iterator)
    0
    >>> next(iterator)
    1
    >>> dir(iterator)
    ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__length_hint__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'next']
    >>> iterator.next()
    2

.. code-block:: python

    >>> map(bool, [None, 0, "", u"", list(), tuple(), dict(), set(), frozenset()])
    [False, False, False, False, False, False, False, False, False]
    >>>

=============== ===============================================================
  memoryview()  # 
  min()         # 返回容器中最小元素
  next()        # 迭代器向下执行一次
  object()      # 类相关
  oct()         # 八进制强制类型转换
  open()        # 上下文管理器
  ord()         # ASCII字符转编码
  pow()         # 求次方
  print()       # 打印任何对象，用于调试代码
  property()    # 类相关
  range()       # 返回整数列表
  repr()        # 将对象字符串化
  reversed()    # 反转，和列表方法reverse()不同之处是生成新的列表
  round()       # 四舍五入求整
=============== ===============================================================

.. code-block:: python

    import hou

    print(kwargs)
    print(type(kwargs))
    print(repr(kwargs))
    print(type(repr(kwargs)))

.. code-block:: python

    >>> round(3.14)
    3.0
    >>> round(3.6)
    4.0
    >>> round(3.5)
    4.0
    >>> round(3.4999)
    3.0
    >>>

================= ===============================================================
  set()            # 元组容器强制转换
  setattr()        # 类相关
  slice()          # 列表的切片
  sorted()         # 排序，和列表方法sort()不同之处是生成新的列表
  staticmethod()   # 类相关
  str()            # 字符串强制类型转换
  sum()            # 求和
  super()          # 类相关
  tuple()          # 将一个可迭代对象转换成元组
  type()           # 返回对象的类型
  vars()           # 
  zip()            # 将两个相同元素个数的列表打包成一个键值对的元组列表
  __import__()     # 用于动态加载类和函数
================= ===============================================================

.. code-block:: python

    >>> print(123)
    123
    >>> type(1)
    <type 'int'>
    >>> type("1")
    <type 'str'>
    >>> type(3 / 2.0)
    <type 'float'>
    >>> type(3 / 2)
    <type 'int'>
    >>> isinstance("1", int)
    False
    >>> int("123")
    123
    >>> bool(8)
    True
    >>>
    >>> str(123)
    '123'
    >>> int("123")
    123
    >>> bin(17)
    '0b10001'
    >>> int("0b10001", 2)
    17
    >>> oct(20)
    '024'
    >>> int("024", 8)
    20
    >>> hex(22)
    '0x16'
    >>> int("0x16", 16)
    22
    >>> str(0.9)
    '0.9'
    >>> float("0.9")
    0.9
    >>> str([0, 1, 2])
    '[0, 1, 2]'
    >>> eval("[0, 1, 2]")
    [0, 1, 2]
    >>>
    >>> reduce(lambda x, y: x + y, range(10))
    45
    >>>
    >>> l1 = range(10)
    >>>
    >>> sl = slice(1, 3, 2)
    >>> l1[sl]
    range(1, 3, 2)
    >>>

.. code-block:: python

    >>> keys = ["name", "age"]
    >>> values = ["Andy", 30]
    >>> zip(keys, values)
    [('name', 'Andy'), ('age', 30)]
    >>> dict(zip(keys, values))
    {'age': 30, 'name': 'Andy'}
    >>> 

----------------
参考文档
----------------

- https://docs.python.org/zh-cn/3/library/functions.html