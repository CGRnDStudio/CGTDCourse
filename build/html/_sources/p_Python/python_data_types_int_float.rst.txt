=============================
Python数据类型：整型 & 浮点型
=============================

------------------
整型
------------------

小整数缓存池：[-5, 257)

算术运算符

.. code-block:: bash

    +, -, *, /, %, //

.. code-block:: bash

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
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero
    >>>


坐井观天：本节知识点
五大基本数据类型
整型
浮点型
字符串
布尔值
None

算术运算符
逻辑运算符
比较运算符

变量
变量命名
下划线命名法 & 驼峰命名法


管中窥豹：延伸阅读
- 掌握字符串所有操作函数
- 掌握所有转义字符
- 熟练使用字符串格式化

Python选择哪个版本？
 - Python 2.x？Python 3.x？
 - x64？x32？

import sys
sys.executable

Python基本数据类型以及操作方法
- 整型
- 浮点型
- 布尔
- 字符串
- 字符串函数
- 字符串格式化
- 字符编码
- 转义字符

数据类型
五大类基本数据类型
int 整型
float 浮点型
string 字符串 取值 format join replace split  转义字符 \n 格式化
bool True False
None

内置函数(学习方法) built-in function
type() 是什么数据类型
dir() 某一个数据类型的属性跟方法
help() 看某一个方法的帮助

算数运算
逻辑运算 and or not 与或非
比较运算 ==，<，>, !=, <=, >=, in, not in, is, is not

计算机编码
ASCII
gb23112
GBK
UNICODE 中间平台
UTF-8

四种数据结构
list 列表 [] 有序的 可迭代的 切片
dict 字典 {key: value}  无序的 可迭代的 散列表
tuple  元组 () 不可变 可以迭代的 切片 有序的
set 集合 {} 元素唯一性

接下来采用ipython来讲解一些Python基本数据类型
a = 5
a = 3.3
a = "andy"
a = True
b = False
a == b

a != b
s = "My Name is Andy"
s2 = "Hello "
s2 + s
s - "Name"
dir(s)
s.capitalize()
s.upper()
s.endswith("y")
s.find("n")
"My name is %s" % "Andy"
"My name is {0}".format("Andy")
"My name is {0}, age is {1}".format("Andy", 28)
"My name is %s, age is %d" % ("Andy", 28)
"流浪地球"
u"流浪地球"
print("My name is Andy.\nMy age is 28.")
print(r"My name is Andy.\nMy age is 28.")
s3 = "Hello Andy  "
s3.strip()
s4 = "Name1 Name2 Name3"
s4.split()
s4.startswith("N")




type()
dir()
help()

print("hello world")
print("123")
print(123)
print("hello")
print("world")
print("how are you?")
print("I'm OK!")
转义字符
print("这是字符串")
print(u"这是字符串")
print("")
print("""
this is a multi-line string.
it has two lines.
""")
print('''
this is a multi-line string.
it has two lines.
''')
\n
单行代码注释
多行代码注释
docstring

常见异常
语法错误
缩进错误
 print("hello world)

int
print(123)
print(1)
print("321")
print(999)
print(99999999999999999999999999999999999999999999)
float
print(3.14159265358979323)
bool
True
False
and or not

算数运算符
比较运算符
逻辑运算符

print(1 + 2)
print(1.0 + 2)
print(10 / 3)
print(10 / 3.0)
print(10.0 / 3.3)
print(10.0 // 3.3)
print(10 / 3)
print(1.1 % 0.3)
print("hello" + "world")
print("hello" * 5)
print(True + True)
print(5 / False)

print(3  > 4)
print(4 < 5)
print(5 = 6)
print(5 == 6)
print(5 is 5)
is VS ==

and
or
not

内置函数
print(123)
type(1)
type("1")
type(3 / 2.0)
type(3 / 2)
isinstance("1", int)
int("123")
bool(8)

解决一个中心问题：数据类型的共性是什么?

内功心法三个内置函数：type() dir() help()

变量
变量命名 下划线命名法 驼峰命名法



Python逻辑运算符的短路规则
如果你了解二进制以及逻辑电路的知识，对逻辑运算符应该不会陌生。十进制数有加减乘除等算术运算，二进制作为另一种进制规则，自然也会有自己的运算方法，这种运算方法叫做逻辑运算。在Python中逻辑运算符有三个and、or和not，对应逻辑电路里的与、或、非门。
短路规则，又称最小化求值。是一种逻辑运算符的求值策略。只有当第一个运算数的值无法确定逻辑运算的结果时，才对第二个运算数进行求值。例如，当and的第一个运算数的值为False时，其结果必定为False；当or的第一个运算数为True时，最后结果必定为True，在这种情况下，就不需要知道第二个运算数的具体值。
那么Python中如何判定一个对象的真假呢？下面列举的是Python中的默认为假值的对象。
●None
●False
●0
●0.0
●0j
●Decimal(0)
●Fraction(0, 1)
●[] - an empty list
●{} - an empty dict
●() - an empty tuple
●'' - an empty str
●b'' - an empty bytes
●set() - an empty set
●an empty range, like range(0)
●objects for which
○obj.__bool__() returns False
○obj.__len__() returns 0
如果不在

用and和or实现三元表达式（也叫三目运算符）
x = 5
y = “A” if x > 0 else “B”
用or提供默认值

两个案例写法
如果一个全整数的列表求最大值与最小值的差，一个全整数的列表求大于9000的数，如果没有返回默认值9000

path in sys.path or sys.path.insert(0, path)
基于这种惰性求值方法，尽可能将需要求值时间短的表达式放前面

运维利器 SpaceSniffer C盘空间总是不够用？








