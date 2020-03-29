=============================
Python容器：列表 []
=============================

容器是对专门用来装其它对象的数据类型的统称。在Python中，有四种最常见的内建容器类型：列表（list）、元组（tuple）、字典（dict）、集合（set）。Python语言内部实现细节也与这些容器息息相关。比如Python的类实例属性、全局变量globals()等都是通过字典类型来存储的。

----------------
列表 list []
----------------

----------------
有序
----------------

----------------
可迭代
----------------

----------------
索引 & 切片
----------------

----------------
列表方法
----------------

.. code-block:: python

    >>> type([])
    <type 'list'>
    >>> dir([])
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>>

在Python 2中，如果你调用 ``range(100000000)`` ，需要等待好几秒才能拿到结果，因为它需要返回一个巨大的列表，花费了非常多的时间在内存分配与计算上。但在Python 3中，同样的调用马上就能拿到结果。因为函数返回的不再是列表，而是一个类型为 ``range`` 的懒惰对象，只有在你迭代它、或是对它进行切片时，它才会返回真正的数字给你。

坐井观天：本节知识点
掌握列表、列表推导

管中窥豹：延伸阅读
# Python基本数据类型以及操作方法
- 列表
- 列表操作函数
- 集合
- 集合操作函数
- 字典
- 字典操作函数
- 列表切片操作
- 列表推导
- 列表迭代
- 字典迭代

l = []
l.append(1)
print(l)
l.extend([1, 2, 3])
print(l)
l.count(1)
l.index(3)
l.pop()
print(l)
l2 = [1, 2, 3, 4, 5]
print(l2)
l2.reverse()
print(l2)
print(l2)
l2.sort()
print(l2)
l3 = [35, 50, 17, 30]
print(l3)
sorted(l3)
print(l3)
print(sorted(l3))
s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 5, 7, 8, 9])
print(s1.union(s2))
s1 = set(["Andy", "Tommy", "Ben", "Gloria", "Dinna"])
s2 = set(["John", "Tommy", "Ben", "Gloria", "Dinna"])
print(s1.difference(s2))
d = {"name": "Andy", "age": 28, "country": "China"}
print(d)
print(d["name"])
d["name"] = "Gloria"
print(d)
d2 = d
print(d)
print(d2)
d2["name"] = "Andy"
print(d)
print(d2)
d2 = d.copy()
print(d)
print(d2)
d2["name"] = "John"
print(d)
print(d2)
print(id(d))
print(id(d2))
l2 = [9, 5, 45, 2, 1]
l3 = l2
print(l2, l3)
l2.append(100)
print(l2, l3)
l4 = l2[:]
print(l2, l4)
l2.append(200)
print(l2, l4)
print(d2)
print(d2["age"])
# print(d2["ages"])
print(d2.get("key", None))
print(d2.has_key("age"))
print(d2.items())
print(d2.keys())
print(d2.values())
print(d2)
d2.pop("age")
print(d2)
d2.update(dict(age=29))
print(d2)
range(5, 0, -1)
g = xrange(1000000)
print(g)
print(g[1000])


基本数据类型
int
float
string
bool
None

type()
dir()
help()

四种组合数据类型
列表 [] list
可变的
切片
迭代 循环
for i in 列表:
    code

元组 () tuple
不可变的

字典 {"key": "value"} dict 
迭代

集合 {""，""} set()  set
元素唯一性

not and or 与或非


if 真假事件:
    code do sth

if 真假事件 and 真假事件:
    code do sth

开发效率比执行效率

built-in function 内置函数

列表

intList = [1, 2, 3]
print(intList)
intList == [1, 2, "3"]
print(intList)
print(type(intList))
nameList = ["andy", "dovfx"]
print(nameList)
complexList = [99, "hello", [1, 2], nameList]
print(complexList)
type(complexList)
print(type(complexList))
print(range(1, 100))
print(range(100))
print(range(1, 100, 5))

切片
numbers = range(10)
print(numbers)
print(numbers[1])
print(numbers[0])
print(numbers[-1])
myList = [numbers, ["a", "b", "c"]]
print(myList[1][1])
myList[-1][1] = "bb"
print(myList)
print(numbers[1:7])
print(numbers[3:])
print(numbers[:3])
print(numbers[-4:-1])
print(numbers[3:-2])
print(numbers[1:7:2])
print(dir(numbers))


方法
dir?
numbers.append(100)
print(numbers)
print(numbers.count(100))

a = ["a", "b", "c"]
numbers.extend(a)
print(numbers)
numbers = range(10)
numbers.append(a)
print(numbers)

print(a.index("b"))
a.append("d")
a.insert(0, "d")
a.pop(0)
a.remove("a")

numbers.reverse()
print(numbers)
reverse() VS reversed()

numbers.sort()
print(numbers)
sort() VS sorted()

l2 = l1[:].sort()
# 浅拷贝与深拷贝
l2 = sorted(l1)

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

列表切片
l3 = [9, 5, 45, 2, 1, 100, 200]
print(l3[0:3])
print(l3[:3])
print(l3[-1])
print(l3[-3:-1])
列表推导
字符串格式化
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


