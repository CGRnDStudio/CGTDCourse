==============================
Houdini VEX：流控制语句
==============================

- 循环语句

    - do statement [while (condition)]
    - for (init; condition; change) statement
    - foreach (type value; array) statement
    - foreach (int index, type value; array) statement
    - while (condition) statement

.. code-block:: python

    for (int n = 0; n < 10; n++) {
        addpoint(0, set(n, 0, 0));
    }

.. code-block:: python

    s@a = "andyvfx";

    foreach (string s; @a) {
        printf("%g\n", s);
    }

.. code-block:: python

    i[]@a = {10, 20, 30, 40, 50, 60};

    foreach (int i; @a) {
        printf(itoa(i) + "\n");
    }

.. code-block:: python

    i[]@a = {10, 20, 30, 40, 50, 60};

    foreach (int i; int v; @a) {
        printf(itoa(i) + "\n");
        printf(itoa(v) + "\n");
    }


- 条件语句

    - if (condition) statement_if_true [else statement_if_false]
    - if (condition) statement_if_true [else if (condition) statement_if_true] else statement_if_false

- break & continue & return

.. code-block:: python

    int max(int a, b) {

        if (a > b) {
            return a;
        }

        return b;
    }

.. code-block:: python

    for (int i = 0; i < sizes; i++) {
        mixamount += getAmount(roughness);

        if (mixamount > 1) {
            break;
        }
    }

.. code-block:: python

    foreach (x; myarray) {

        if (x < 10) continue;
        ...
    }

- 与或非 && || !

.. code-block:: python

    if (@ptnum % 2 == 0) {
        print("%g\n", @ptnum);
    }


    if (@ptnum % 2) {
        print("%g\n", @ptnum);
    }

条件表达式

@Cd = @ptnum ? 1 : 0

while & do while的区别

While Loop

Do While Loop

Foreach Loop

For Loop

.. code-block:: python

    int i = 0;

    for (float foo = 1; foo <= 128; foo *= 2, i++) {
        vector pos = point(0, "P", i);
        --pos.y;
        setpointattrib(0, "P", i, pos);
    }