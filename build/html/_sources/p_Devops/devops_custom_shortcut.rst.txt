=========================================
Windows自定义快捷方式
=========================================

Nuke打开频繁遇到下面这个问题。

Frame Server failed to bind TCP port 5559 and found existing Frame Server processes. Would you like Nuke to attempt to kill these processes?

软件启动一般可以带一些参数起到不同启动的效果，往往我们需要自定义一些软件启动的快捷方式。默认NukeX的启动目标是这样的。

.. code-block:: python

    "C:\Program Files\Nuke12.1v2\Nuke12.1.exe" --nukex

可以通过右键新建>快捷方式，写入启动内容。

.. code-block:: python

    "C:\Program Files\Nuke11.2v3\Nuke11.2.exe" --nukex --disable-nuke-frameserver

比如启动Maya关闭Console窗口，可以这样干。

.. code-block:: python

    "C:\Program Files\Autodesk\Maya2018\bin\maya.exe" -hideConsole


