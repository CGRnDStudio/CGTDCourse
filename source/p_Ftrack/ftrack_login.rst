=============================
Ftrack Python API
=============================

创建用户

.. code-block:: python

    newUser = session.create("User", {"username": "huweiguo@do-vfx.com"})

    session.commit()

创建任务

.. code-block:: python

    shot = session.query("Shot where name is 'f_CTS049'").first()

    newTask = session.create("Task", {"name": "fx_autosphere", "parent": shot})

    session.commit()

