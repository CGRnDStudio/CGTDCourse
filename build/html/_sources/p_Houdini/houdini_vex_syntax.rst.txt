==============================
Houdini VEX：基础语法
==============================

VEX脚本是VOP系统的编程语言的表达方式，而VOP系统是VEX脚本的可视化操作方式。

Point Wrangle、Primitive Wrangle、Vertex Wrangle都是Attribute Wrangle节点。

Point VOP、Primitive VOP、Vertex VOP都是Attribute VOP节点。

VEX语法规则和C语言接近，和Python有很大区别，下面列出一些和Python语法上的不同点，以便区分是VEX脚本还是Python脚本。

- VEX行结尾使用分号;
- VEX代码块使用花括号{}
- VEX声明变量定义变量类型
- VEX声明函数定义函数返回值类型
- VEX注释使用正斜杠，单行//，多行/*multi-code*/

Houdini中可以在Attribute Wrangle节点（节点网络中TAB键输入aw，后面简称aw节点）来编写VEX代码，这个节点很神奇，官网文档有说明它有一种内建的上下文处理机制，参数Run Over切换五种模式会得到不同的结果。

- Detail(only once)
- Primitives
- Points
- Vertices
- Numbers

默认参数Points意味代码将在每个点循环执行，虽然你代码并没有写循环，只有有任何处理点的操作即会循环。

创建个box，连接一个aw节点，写入如下代码：

.. code-block:: python

    printf("hello vex\n");
    printf("%d\n", @ptnum);

    // hello vex
    // 0
    // 1
    // 2
    // 3
    // 4
    // 5
    // 6
    // 7

* 变量声明

.. code-block:: python

    vector <variableName>;

* 属性 VS 变量

属性实际也是变量，唯一的区别是属性是定义在几何体上的变量而已，用来处理几何体数据。

声明属性的时候只要在变量前加@符号即可，当然会有一些小技巧。

属性有内置属性和自定义属性之分。

* 内置属性

Houdini中有很多内置属性，也就是几何体有一些约定俗成的属性，这些属性不需要声明类型就可以使用，Houdini能自动识别它们的数据类型，没有特别说明都假定为浮点型。

内置属性都可以在VOP系统中找到对应的参数入口。

============= =====================================================================================================================
内置类型       内置属性
int           @id, @ptnum, @primnum, @vtxnum, @numpt, @numprim, @numvtx, @group_*, @resx, @resy, @resz
float         @pscale, @Time, @Frame
string        @name
vector        @P, @Cd, @N, @force, @rest, @up, @uv, @v
vector4       @orient
============= =====================================================================================================================

更多内置属性可参考文档：http://www.sidefx.com/docs/houdini/model/attributes.html

* 自定义属性

自定义属性在声明的时候@符号前加属性的数据类型，比如v@表示向量，f@表示浮点数，i@表示整数等，后面引用属性的时候就可以像内置属性一样不用加具体的数据类型，如果没有声明变量的类型，则默认以浮点型作为类型，自定义属性最好是声明具体的类型。

    - v@vectorAttributeName;
    - f@floatAttributeName;
    - i@intAttributeName;

属性一般都有创建、设置、获取三种行为，比如给当前几何体添加法线属性（法线属性@N是一种内置属性）。

.. code-block:: python

    @N = {0, 1, 0};
    @N = set(0, 1, 0);
    @N = @P;

或者自定义属性

.. code-block:: python

    v@pos = @P;
    f@y_pos = @P.y;

变量声明vector <variableName>和自定义属性v@attriName区别在于变量只会在当前代码中发挥作用，而属性会传递给几何体，作为数据流的一部分可以传递给下游节点，是使用变量还是属性的原则就是数据是否要给到下游，如果不需要就使用变量，因为几何体上的属性都是需要占用硬件资源的。

* 数据类型

============= ============ ========================================================================
变量声明       自定义属性     案例
int            i@           1, 2, 3
float          f@           3.14, 9.8
vector2        u@           {0, 0}, {0.1, 0.2}
vector         v@           {0, 0, 0}
vector4        p@           {0, 0, 0, 0}
array          i/f/s[]@     {1, 2, 3, 4, 5, 6, 7, 8}
matrix2        2@           {{0, 1}, {2, 3}}
matrix3        3@           {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}
matrix         4@           {{1, 0, 0, 1}, {0, 1, 0, 1}, {0, 0, 1, 1}, {0, 0, 1, 1}}
string         s@           "hello world"
============= ============ ========================================================================

* 数组

数组在VEX中是一种极其重要的容器，不管是向量还是四元素都离不开数组的组织数据。

* 字符串

* 切片

切片很容易理解，和Python中列表切片概念是一样的，通过元素的index来获取区间。

* 结构体

* 点操作符

- .x 或 .u 指向vector2变量或属性的第一个元素。
- .x 或 .r 指向vector和vector4变量或属性的第一个元素。
- .y 或 .v 指向vector2变量或属性的第二个元素。
- .y 或 .g 指向vector和vector4变量或属性的第二个元素。
- .z 或 .b 指向vector和vector4变量或属性的第三个元素。
- .w 或 .a 指向vector4变量或属性的第四个元素.

如果是矩阵，则

- .xx 指向[0][0]元素。
- .zz 指向[2][2]元素。
- .ax 指向[3][0]元素。

--------------------
参考文档
--------------------

- http://www.sidefx.com/docs/houdini/vex/index.html
- http://www.sidefx.com/docs/houdini/vex/lang.html
- http://www.sidefx.com/docs/houdini/vex/snippets.html
