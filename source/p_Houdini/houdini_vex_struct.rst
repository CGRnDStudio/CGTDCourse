==============================
Houdini VEX：结构体
==============================

.. code-block:: python

    struct box {
        vector size = {1, 1, 1};
        vector center = {0, 0, 0};
        float uscale = 1;

        void create() {
            vector pos[] = {
                {0.5, 0.5, 0.5},
                {0.5, 0.5, 0.5},
                {0.5, 0.5, 0.5},
                {0.5, 0.5, 0.5},
                {0.5, 0.5, 0.5},
                {0.5, 0.5, 0.5},
                {0.5, 0.5, 0.5},
                {0.5, 0.5, 0.5}
            };
            foreach(vector pt; pos) {
                addpoint(0, pt);
            }
        }
    }


.. code-block:: python

    #include <box.h>
    box mybox;
    printf("%g\n", mybox.size);
    mybox->create();
