==============================
Houdini进度条
==============================

Houdini Python API中提供hou.InteruptableOperation类来处理进度条，还有一种进度条方案是通过PyQt来实现。此文档介绍一下官方提供的接口的使用方法。

如果只有一个循环任务可以使用下面的套路代码，将time.sleep(1)替换成任务代码。

.. code-block:: python

    import time
    import hou

    num = 5

    with hou.InterruptableOperation("Performing Tasks", open_interrupt_dialog=True) as operation:

        for i in range(num):
            # Perform task here.
            time.sleep(1)

            # Update operation progress.
            percent = float(i) / float(num)
            operation.updateProgress(percent)

如果有两个循环嵌套的子任务，可以用下面的套路代码模板来写，将time.sleep(1)替换成任务代码即可。

.. code-block:: python

    import time
    import hou

    taskNum = 5
    subTaskNum = 5

    with hou.InterruptableOperation("Performing", "Performing Tasks", open_interrupt_dialog=True) as operation:

        for i in range(taskNum):
            # Update long operation progress.
            longPercent = float(i) / float(taskNum)
            operation.updateLongProgress(longPercent, long_op_status="Performing Tasks %d%%" % (longPercent * 100))

            # Start the sub-operation.
            with hou.InterruptableOperation("Performing Task %i" % i) as suboperation:
                for j in range(subTaskNum):
                    # Update sub-operation progress.
                    percent = float(j) / float(subTaskNum)
                    suboperation.updateProgress(percent)

                    # Perform subtask here.
                    time.sleep(1)
