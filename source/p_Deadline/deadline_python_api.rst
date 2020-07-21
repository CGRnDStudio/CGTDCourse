=============================
Deadline渲染农场提交农场接口
=============================

使用Deadline Python API提交任务需要开启deadlinewebservice.exe服务。

.. code-block:: python

    import sys
    sys.path.insert(0, r"Y:\Program\DeadlineRepository10\api\python")
    from Deadline.DeadlineConnect import DeadlineCon as Connect
    con = Connect("farm.do-vfx.com", 8082)

    job = con.Jobs.GetJob("5bfce04f4096fe78c0f6d640")

    print(job)
