==============================
Houdini VEX：数组函数
==============================

数组特点是有序的，存储相同类型的数据集合。

索引与切片。

数组赋值

int a[];
i[]@a;
{}
array()

数组函数

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

数组循环

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