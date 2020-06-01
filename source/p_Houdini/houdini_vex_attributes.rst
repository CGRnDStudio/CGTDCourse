==============================
Houdini VEX：属性
==============================



创建属性

.. code-block:: python

    int @num = 100;

    i@num = 100;

    int @num[];

    i[]@num = {100, 200};


两种方案的区别有一些，i@num可以使用表达式运算或者函数返回值，数组属性不简写不能赋初始值。

.. code-block:: python

    vector @up = {0, 1, 0};
    v@up = set(0, 1, 0);

内置属性不用指定数据类型，比如@ptnum，@N等，自定义属性如果不指定数据类型，默认初始化为浮点型数据。

所以为了和变量创建区别开推荐使用简写创建属性的方案。

i@i = 100;
f@pi = 3.14;
u@v1 = {1.0, 2.0};
v@v2 = set(1.0, $PI, 2.0);
p@
2@
3@
4@
s@

数组属性

i[]@
f[]@
s[]@

函数添加属性

.. code-block:: python

    addpointattrib(0, "Cd", {0, 0, 0});
    addvertexattrib(0, "Cd", {0, 0, 0});
    addprimattrib(0, "Cd", {0, 0, 0});
    adddetailattrib(0, "Cd", {0, 0, 0});

修改属性

.. code-block:: python

    setpointattrib(0, "Cd", 0, {0, 0, 0});
    setvertexattrib(0, "Cd", 0, {0, 0, 0});
    setprimattrib(0, "Cd", 0, 0, {0, 0, 0});
    setdetailattrib(0, "Cd", {0, 0, 0});

获取属性

.. code-block:: python

    float f1 = @P.y;
    float f2 = @opinput1_Cd.y;
    float f3 = v@opinput1_v1.y;
    vector c1 = point(1, "Cd", @ptnum);
    vector c2 = prim(1, "Cd", 0);
    vector c3 = vertex(1, "Cd", 0);
    vector c4 = detail(1, "Cd", 0);

全局属性

.. code-block:: bash

    printf("%g\n", $PI);
    printf("%g\n", $E);
    printf("%g\n", @Frame);
    printf("%g\n", @Time);
    printf("%g\n", @Timeinc);
    printf("%g\n", @SimFrame);
    printf("%g\n", @SimTime);

内在属性

Intrinsic内在属性只有prim和detail上才会存在

prim() 读取属性
primintrinsic() 读取属性
setprimintrinsic() 设置属性

属性相关函数
