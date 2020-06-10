==============================
Houdini OpenCL简单介绍
==============================

.. code-block:: python

    kernel void up(int P_length, global float *P) {
        int idx = get_global_id(0);

        if (idx >= P_length) {
            return;
        }

        float3 pos = vload3(idx, P);

        pos.y += 1;

        vstore3(pos, idx, P);
    }

OpenCL不能创建属性。