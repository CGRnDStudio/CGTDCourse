=============================
Python数据类型：布尔值 & 空值
=============================

- 布尔值 True & False

比较运算符

==, <, >, !=, <=, >=, in, not in, is, is not

逻辑运算符

.. code-block:: python

    and
    or
    not

Python逻辑运算符的短路规则

如果你了解二进制以及逻辑电路的知识，对逻辑运算符应该不会陌生。十进制数有加减乘除等算术运算，二进制作为另一种进制规则，自然也会有自己的运算方法，这种运算方法叫做逻辑运算。在Python中逻辑运算符有三个and、or和not，对应逻辑电路里的与、或、非门。

短路规则，又称最小化求值。是一种逻辑运算符的求值策略。只有当第一个运算数的值无法确定逻辑运算的结果时，才对第二个运算数进行求值。例如，当and的第一个运算数的值为False时，其结果必定为False；当or的第一个运算数为True时，最后结果必定为True，在这种情况下，就不需要知道第二个运算数的具体值。

那么Python中如何判定一个对象的真假呢？下面列举的是Python中的默认为假值的对象。

.. code-block:: python

    None
    False
    0
    0.0
    0j
    Decimal(0)
    Fraction(0, 1)
    [] - an empty list
    {} - an empty dict
    () - an empty tuple
    '' - an empty str
    b'' - an empty bytes
    set() - an empty set

一个对象的真假状态可以通过内置函数bool()来做检测，在写if条件的时候可以通过对象的真假状态来直接判断，而无需比较。

不建议的代码：

.. code-block:: python

    if var == None:
    if var == 0:
    if var == []:
    if var == "":

建议的代码：

.. code-block:: python

    if not var:

用and和or实现三元表达式（也叫三目运算符）

.. code-block:: python

    x = 5
    y = "A" if x > 0 else "B"

用or提供默认值

.. code-block:: python

    path in sys.path or sys.path.insert(0, path)

基于这种惰性求值方法，尽可能将需要求值时间短的表达式放前面。

- 空值 None

None是Python中一个特殊的值，虽然它不表示任何数据，但仍然具有重要的作用。自定义函数如果没有使用return，则默认返回值是None。
