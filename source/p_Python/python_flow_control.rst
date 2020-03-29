=============================
Python流控制语句
=============================

Python流控制语句包括if条件判断语句、for循环语句、while循环语句以及try异常中断语句。

--------------
if条件判断语句
--------------

if语句如果条件太多，可以使用字典替代方案。

.. code-block:: python

    # if语句的几种常见写法
    if condition:
        statement block

    if condition:
        statement block
    else:
        statement block

    if condition:
        statement block
    elif condition:
        statement block
    ...
    else:
        statement block

--------------
for循环语句
--------------

.. code-block:: python

    # for语句的写法
    for element in iterable:
        statement block

    for element in iterable:
        statement block
    else:
        statement block

break与continue的区别

* break中断整个循环语句
* continue中断本次循环，继续下一次循环

--------------
while循环语句
--------------

while循环需要注意避免死循环，语句块中需要有自增或自检以结束循环条件。

.. code-block:: python

    # while语句的写法
    while condition:
        statement block

---------------
try异常中断语句
---------------

.. code-block:: python

    # try语句的写法

    try:
        statement block
    except:
        statement block

    try:
        statement block
    except A:
        statement block
    except B:
        statement block
    except:
        statement block
    else:
        statement block
    finally:
        statement block

.. code-block:: python

    try:
        1 / 0
    except ZeroDivisionError as e:
        print(e)

异常捕获对于调试代码并不是一件友好的事情，经常在调试代码过程中我们会避免使用try语句以获得代码异常的详细信息。
异常也可以自定义，可以通过关键字raise来抛出异常。

.. code-block:: python

    def checkAbs(x):

        if not isinstance(x, (int, float)):
            raise TypeError("x only support int or float")

        if x >= 0:
            return x
        else:
            return -x


坐井观天：本节知识点

异常中断

三元赋值法
冒号 + 严格缩进 = 代码块
条件判断语句
if
循环语句
for
while

break 完全中断循环
continue 只中断本次循环

for i in range(10):
     if i == 5:
         break
     print(i)

for i in range(10):
     if i == 5:
         continue
     print(i)


函数中return起到中断作用

if语句的三种写法

if condition:
    code block

if condition:
    code block
else:
    code block

多个条件判断
if condition:
    code block
elif condition:
    code block
elif condition:
    code block
else:
    code block

PS: condition如何写? 逻辑运算符, 内置函数bool()

不要这样写
if a == False:
if a == 0:
if a == None:
if a == []:
if a == “”:
建议写成
if not a:

变量赋值
a = 1
a = "hello"
print(a + "world")
print(a * 5)

a = 10
print(a * 5)

a += 1
print(a)

a -= 1
print(a)
a, b = 1, 2
a, b = b, a
%history
input?
input("请输入:")
# 转换为字符串
raw_input("请输入") 
userSays = raw_input("请输入:") or "nothing"

# 三元赋值法
"hello" if True else "world"
"hello" if 1 > 2 else "world"

a = input("请输入一个整数：")

if a % 2 == 0:
    print("a是一个偶数")
else:
    print("a是一个奇数")

a = -2
if a > 0:
    print("a是正数")
elif a < 0:
    print("a是负数")
else:
    print("a是零")

for循环语句


while循环语句

while condition:
    code
    自增或者自减以满足条件避免死循环

a = 1
while a < 10:
    print("now a is ", a)
    a += 1

import this
import antigravity
import datetime
print(datetime.datetime.now())

as名称空间
import datetime as dt
print(dt.datetime.now())
from datetime import datetime as dt
print(dt.now())
import random
random.randint?


异常中断

try:
    if True:
        raise Exception("Error Message!")
except Exception as ex:
    print("Exception:", ex.message)
else:
    print("Else....")
finally:
    print("Finally...")


