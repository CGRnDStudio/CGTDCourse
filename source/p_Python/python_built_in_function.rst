=============================
Python内置函数
=============================

Python内置函数也叫Python内建函数（built-in function），内置函数大约有60来个，都非常有用。

* print() # 打印任何对象
* len() # 求容器元素个数
* enumerate() # 索引遍历函数

.. code-block:: python

    for i, item in enumerate(myList):
        print(i, "-->", item)

* int() & float() & str() & bool()


* id() # 返回对象的内存地址
* type() # 获取对象的类型
* dir() # 获取对象的属性和方法
* help() # 获取对象具体属性与方法的帮助文档
* eval() # 将一个字符串当成一个表达式来执行，返回表达式执行后的结果。
* exec() # 将一个字符串当成程序来执行。

* max() & min() & sum()

* abs()

* hex() & oct() & bin()

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


管中窥豹：延伸阅读
https://docs.python.org/zh-cn/3/library/functions.html


abs() 求绝对值
abs(-100)
complex() 复数
divmod() 求商和余数
pow() 求次方

all(iterable) 所有元素都为真，则返回True
any(iterable) 只要有一个元素为真，则返回True

类型转换
bin() 十进制>二进制
chr() 字符
hex() 十进制>十六进制
oct() 十进制>八进制
ord() 
bool() 测试一个对象是True还是False
int() 整型
float() 浮点型
str() 转字符串
eval()
list()
set()
dict()
tuple()

str(123)
int("123")
bin(17)
int("0b10001", 2)
oct(20)
int("024", 8)
hex(22)
int("0x16", 16)
str(0.9)
float("0.9")
str([0, 1, 2])
eval("[0, 1, 2]")



判断
callable() 是否是一个函数
isinstance() 是否是某一类数据类型
issubclass()

len() 元素数量
enumerate() 返回迭代器的index
open() 上下文管理器

min() 最小元素
max() 最大元素
sum() 求和

type() 获取实例对象数据类型
dir() 获取实例对象的属性与方法
help() 获取某一类方法的帮助文档

filter()
map()
reduce()
range()
xrange()
reversed()
sorted()

map(bool, [None, 0, "", u"", list(), tuple(), dict(), set(), frozenset()])

filter(bool, [1, 0, 2, "", [], 3])

format() & str.format()
format(1/2.43, "0.4f")
"{:0.4f}".format(1/2.43)

input()
iter()
round()
zip()
