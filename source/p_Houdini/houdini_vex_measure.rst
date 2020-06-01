==============================
Houdini VEX：测量函数
==============================

- vector  relbbox(<geometry>geometry, vector position)
- vector  relbbox(<geometry>geometry, string primgroup, vector position)
- vector  relbbox(vector position)

distance()

.. code-block:: python

    @Cd = relbbox(geoself(), @P);

- vector  getbbox_size(<geometry>geometry)
- vector  getbbox_size(<geometry>geometry, string primgroup)

.. code-block:: python

    vector size = getbbox_size(geoself());
    printf("%g", size);
