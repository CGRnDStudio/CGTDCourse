==============================
Houdini VEX：数组函数
==============================

数组是存储相同类型数据的容器，数组的特点是有序的，有序性决定了数组具有索引与切片的功能。

- 初始化

数组在变量或属性初始化的时候如果没有给初始值，也不会警告或报错，默认初始值是空数组，数组初始化一般是通过花括号{}或者数组函数array()。 

.. code-block:: bash

    int a[];
    i[]@b;
    int c[] = {1, 2, 3};
    i[]@d = {100, 200, 300};
    int e[] = array(0, $PI, 0);

    printf("%g\n", a);
    printf("%g\n", @b);
    printf("%g\n", c);
    printf("%g\n", @d);
    printf("%g\n", e);

    vector color[] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

- 索引与切片

.. code-block:: bash

    int array1[] = {100, 200, 300, 400, 500};

    printf("%g\n", array1[:2]);
    printf("%g\n", array1[-2:]);
    printf("%g\n", array1[::-1]);
    printf("%g\n", array1[-1:-3:-1]);
    printf("%g\n", array1[1::2]);
    printf("%g\n", array1[1:len(array1):2]);

- 数组函数

    - void append(<type>&array[], <type>value)
    - int [] argsort(<type>value[])
    - <type>[] array(...)
    - void insert(string &str, int index, string value)
    - int isvalidindex(<type>&array[], int index)
    - int len(<type>array[])
    - <type> pop(<type>&array[])
    - void push(<type>&array[], <type>value)
    - <type> removeindex(<type>&array[], int index)
    - int removevalue(<type>&array[], <type>value)
    - <type>[] reorder(<type>values[], int indices[])
    - void resize(<type>&array[], int size)
    - <type>[] reverse(<type>values[])
    - <type>[] slice(<type>s[], int start, int end)
    - <type>[] slice(<type>s[], int start, int end, int step)
    - int [] sort(int values[])

- 循环迭代

    - foreach (index, value; array) statement;
    - foreach (int index; element_type value; array) statement;

.. code-block:: python

    int an_array[] = {1, 2}

    foreach (int num; an_array) {
        printf("%d", num);
    }

    string days[] = { "Mon", "Tue", "Wed", "Thu", "Fri" }
    foreach (int i; string name; days) {
        printf("Day number %d is %s", i, name);
    }

- 类型转换

.. code-block:: bash

    vector pos = {1.0, 2.0, 3.0};
    float a[] = set(pos);
    vector color = set(a);

参考文档：

- http://www.sidefx.com/docs/houdini/vex/arrays.html