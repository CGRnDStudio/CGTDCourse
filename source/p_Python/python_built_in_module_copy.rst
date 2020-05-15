=============================
Python内置模块：copy
=============================

内置模块copy的存在主要为了深度拷贝，那么什么是深度拷贝呢？

深度拷贝会递归拷贝所有深度成员。

.. code-block:: python

    >>> import copy
    >>> type(copy)
    <type 'module'>
    >>> dir(copy)
    ['Error', 'PyStringMap', '_EmptyClass', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_copy_dispatch', '_copy_immutable', '_copy_inst', '_copy_with_constructor', '_copy_with_copy_method', '_deepcopy_atomic', '_deepcopy_dict', '_deepcopy_dispatch', '_deepcopy_inst', '_deepcopy_list', '_deepcopy_method', '_deepcopy_tuple', '_keep_alive', '_reconstruct', '_test', 'copy', 'deepcopy', 'dispatch_table', 'error', 'name', 't', 'weakref']
    >>> help(copy.deepcopy)
    Help on function deepcopy in module copy:

    deepcopy(x, memo=None, _nil=[])
        Deep copy operation on arbitrary Python objects.

        See the module's __doc__ string for more info.

    >>>

存在深度拷贝主要原因是可变数据类型可能会触碰到这个问题。

.. code-block:: python

    >>> l1 = [1, [2, 3], 4]
    >>> l2 = l1[:]
    >>> l1
    [1, [2, 3], 4]
    >>> l2
    [1, [2, 3], 4]
    >>> id(l1)
    52764264
    >>> id(l2)
    52762824
    >>> id(l1[1])
    52786560
    >>> id(l2[1])
    52786560
    >>> l1.append(5)
    >>> l1
    [1, [2, 3], 4, 5]
    >>> l2
    [1, [2, 3], 4]
    >>> l1[1].append(100)
    >>> l1
    [1, [2, 3, 100], 4, 5]
    >>> l2
    [1, [2, 3, 100], 4]

上面代码是一个浅拷贝的例子，不经意间你的代码就会出现问题，如果用copy模块呢？

.. code-block:: python

    >>> import copy
    >>> l1
    [1, [2, 3, 100], 4, 5]
    >>> l3 = copy.deepcopy(l1)
    >>> id(l1)
    52764264
    >>> id(l3)
    52786520
    >>> id(l1[1])
    52786560
    >>> id(l3[1])
    52788600
    >>> l1[1].pop()
    100
    >>> l1
    [1, [2, 3], 4, 5]
    >>> l3
    [1, [2, 3, 100], 4, 5]
    >>>
