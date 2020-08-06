=========================================
Katana自定义节点菜单
=========================================

.. code-block:: python

    from Katana import UI4, NodegraphAPI
    from UI4.FormMaster.NodeActionDelegate import (BaseNodeActionDelegate, RegisterActionDelegate)
    from UI4.Manifest import QtCore, QtGui, QtWidgets


    class MyNodeActionDelegate(BaseNodeActionDelegate.BaseNodeActionDelegate):
        class _SelectNodeAction(QtWidgets.QAction):

            def __init__(self, parent, node):
                QtWidgets.QAction.__init__(self, 'Select "%s"' % node.getName(), parent)

                self.__node = node
                if node:
                    self.triggered.connect(self.__triggered)
                self.setEnabled(self.__node is not None
                                and not self.__node.isLocked(True))

            def __triggered(self, checked):
                NodegraphAPI.SetNodeSelected(self.__node, True)

        class _DeselectNodeAction(QtWidgets.QAction):

            def __init__(self, parent, node):
                QtWidgets.QAction.__init__(self, 'Deselect "%s"' % node.getName(), parent)

                self.__node = node
                if node:
                    self.triggered.connect(self.__triggered)
                self.setEnabled(self.__node is not None
                                and not self.__node.isLocked(True))

            def __triggered(self, checked):
                NodegraphAPI.SetNodeSelected(self.__node, False)

        def addToContextMenu(self, menu, node):
            menu.addAction(self._SelectNodeAction(menu, node))
            menu.addAction(self._DeselectNodeAction(menu, node))

        def addToWrenchMenu(self, menu, node, hints=None):
            pass


    RegisterActionDelegate("CameraCreate", MyNodeActionDelegate())


- https://support.foundry.com/hc/en-us/articles/208838305-Q100108-Adding-custom-menu-items-to-the-context-menu-of-nodes