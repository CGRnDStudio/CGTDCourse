==============================
Houdini VEX：体积函数
==============================

- vector volumegradient(<geometry>geometry, int primnum, vector pos) // 体积梯度
- vector volumegradient(<geometry>geometry, string volumename, vector pos) // 体积梯度
- float volumesample(<geometry>geometry, int primnum, vector pos) // 体积采样
- float volumesample(<geometry>geometry, string volumename, vector pos) // 体积采样

.. code-block:: python

    float sample = volumesample(1, 0, @P);

    if (sample < 0) {
        removepoint(0, @ptnum);
    }
