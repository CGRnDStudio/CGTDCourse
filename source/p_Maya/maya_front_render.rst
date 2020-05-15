==============================
Maya前台渲染脚本解决方案
==============================

一般来说前台渲染调用RenderIntoNewWindow或者renderWindowRenderCamera命令即可，批量渲染写个for循环问题不大，下面是Python与MEL两种写法。

.. code-block:: python

    # Python
    import maya.cmds as cmds
    import maya.mel as mel

    for i in range(1, 241):
        cmds.currentTime(i)
        mel.eval("renderWindowRenderCamera redoPreviousRender renderView persp;")

.. code-block:: bash

    // MEL
    for (int $i = 1; $i <= 240; $i++) {
        evalDeferred("currentTime $i;");
        evalDeferred("RenderIntoNewWindow;");
    }

但是遇到Redshift渲染器的时候，上面的for循环会报渲染占用的错误，解决方案可以在Render Settings中写Post render frame MEL，将下面的任何一句MEL脚本写到此设置中，在点击Render View窗口渲染的时候会自动渲染下一帧，渲染的序列在工程路径/images/tmp中，简单实现前台批量渲染的功能，结束渲染需要按ESC中断。

.. code-block:: bash

    // MEL
    int $frame = `currentTime -q`; evalDeferred("currentTime ($frame + 1);"); evalDeferred("RenderIntoNewWindow;");
    int $frame = `currentTime -q`; evalDeferred("currentTime ($frame + 1);"); evalDeferred("renderWindowRenderCamera redoPreviousRender renderView persp;");