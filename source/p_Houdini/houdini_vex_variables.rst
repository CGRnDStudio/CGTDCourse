==============================
Houdini VEX：变量
==============================


变量

数据类型

int
float
vector2
vector
vector4
array
struct
matrix2
matrix3
matrix
string
bsdf

变量命名

26个字母大小写，阿拉伯数字以及下划线，不能以数字开头，不能使用保留字

.. code-block:: bash

    int i = 100;
    float pi = 3.14;
    // vector分量都是浮点型数据
    vector2 v1 = {1.0, 2.0};
    vector v2 = {1.0, 2.0, 3.0};
    vector4 v3 = {1, 2, 3, 4};
    // matrix中括号可要可不要，最好是便于阅读
    matrix2 m1 = {{0, 1}, {1, 0}};
    matrix2 m2 = {0, 1, 2, 3};
    matrix3 m3 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    matrix m4 = {{1, 2, 3, 0}, {4, 5, 6, 0}, {7, 8, 9, 0}, {10, 11, 12, 0}};
    string s = "Andy";

数组类型是有序的同类型数据的组合。

可以声明空数组
.. code-block:: python

    int a1[];
    int a2[] = {};
    int a3[] = array();
    printf("%g\n", a1);
    printf("%g\n", a2);
    printf("%g\n", a3);

{}和array()区别，array()中可以是变量，花括号中只能是数值。
