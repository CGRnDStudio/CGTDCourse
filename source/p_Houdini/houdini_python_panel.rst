==============================
Houdini Python Panel
==============================

Interfaces

Toolbar Menu

Pane Tab Menu


.. code-block:: python

    from hutil.Qt import QtWidgets

    def onCreateInterface():
        widget = QtWidgets.QPushButton("Create Explosion NOW!")
        return widget
