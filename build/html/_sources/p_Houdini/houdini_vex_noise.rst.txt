==============================
Houdini VEX：噪波函数
==============================

- float  rand(float seed)
- vector2  rand(float seed)
- vector  rand(float seed)
- vector4  rand(float seed)
- ...

.. code-block:: python

    @Cd = rand(@ptnum);
    @Cd = rand(@primnum);
