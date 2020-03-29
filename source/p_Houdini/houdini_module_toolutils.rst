==============================
Houdini模块：toolutils
==============================

.. code-block:: python

    import toolutils

    scene_viewer = toolutils.sceneViewer()
    selected_objects = scene_viewer.selectObjects("Select a camera and press Enter", allowed_types = ["cam"])
    print(selected_objects)
