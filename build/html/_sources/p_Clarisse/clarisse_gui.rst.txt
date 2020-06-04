=========================================
Clarisse Python开发界面
=========================================

GUI依然是通过Python代码来实现，同样的道理也有两种方案，第一种方案是用Clarisse封装的GUI库，以Gui开头的Class，它封装的比较全面，可以一用，另一种方案就是用Python中PyQt模块。

.. code-block:: python

    window = ix.api.GuiWindow(ix.application, 0, 0, 640, 480)
    window.show()
    while window.is_shown(): ix.application.check_for_events()

.. code-block:: python

    class CustomButton(ix.api.GuiPushButton):
        def __init__(self, parent, x, y, w, h, label):
            ix.api.GuiPushButton.__init__(self, parent, x, y, w, h, label)
            self.connect(self, "EVT_ID_PUSH_BUTTON_CLICK", self.on_click)

        def on_click(self, sender, evtid):
            name = list.get_selected_item_name()
            
            if name == "Cube":
                ix.cmds.CreateObject("box", "GeometryBox", "Global", "project://scene")
                print("Created a cube success!!!")
            elif name == "Sphere":
                ix.cmds.CreateObject("sphere", "GeometrySphere", "Global", "project://scene")
                print("Created a sphere success!!!")

    if __name__ == "__main__":
        app_x = ix.application.get_event_window().get_position()[0]
        app_y = ix.application.get_event_window().get_position()[1]
        app_w = ix.application.get_event_window().get_width()
        app_h = ix.application.get_event_window().get_height()

        window_x = 150
        window_y = 30

        window = ix.api.GuiWindow(ix.application,
                                  app_x + (app_w - window_x) / 2,
                                  app_y + (app_h - window_y) / 2,
                                  window_x,
                                  window_y,
                                  "Create Object")

        list = ix.api.GuiListButton(window, 0, 0, 100, 30)
        list.add_item("Cube")
        list.add_item("Sphere")
        btn = CustomButton(window, 100, 0, 50, 30, "OK")

        window.show()

        while window.is_shown():
            ix.application.check_for_events()

.. code-block:: python

    for method in dir(ix.api):
        if "EVT_" in method:
            print(method)
