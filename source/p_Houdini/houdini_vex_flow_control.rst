==============================
Houdini VEX：流控制语句
==============================

* 循环语句

.. code-block:: python

    do statement [while (condition)]

.. code-block:: python

    for (init; condition; change) statement

.. code-block:: python

    for (int n = 0; n < 10; n++) {
        addpoint(0, set(n, 0, 0));
    }

.. code-block:: python

    foreach (value; array) statement
    foreach (index, value; array) statement

.. code-block:: python

    while (condition) statement

* 条件语句

if (condition) statement_if_true [else statement_if_false]
if (condition) statement_if_true [else if (condition) statement_if_true] else statement_if_false

* return & break & continue

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
