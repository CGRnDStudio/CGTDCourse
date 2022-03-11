==============================
Nuke TCL
==============================

.. code-block:: python

    [file dirname [value root.name]] # 当前nuke文件所在的文件夹
    [join [lrange [split [file dirname [value root.name]] /] 0 end-1] /] # 当前nuke文件所在文件夹的上一个层级

参考文档：

- http://www.jeangjenq.com/tcl-python-snippets/