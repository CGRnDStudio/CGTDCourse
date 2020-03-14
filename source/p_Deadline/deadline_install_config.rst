=============================
Deadline安装、配置与使用
=============================


------------------
坐井观天: 知识体系
------------------

::::::::::::::::::::::
Deadline服务器部署搭建
::::::::::::::::::::::

- DeadlineRepository10\plugins\Houdini\Houdini.param
- Configure Plugins
- deadlinewebservice.exe http://localhost:8082/

.. code-block:: python

    import sys
    sys.path.insert(0, r"Y:\Program\DeadlineRepository10\api\python")
    from Deadline.DeadlineConnect import DeadlineCon as Connect
    con = Connect("farm.do-vfx.com", 8082)
    
    job = con.Jobs.GetJob("5bfce04f4096fe78c0f6d640")
    
    print(job)


远程控制 开启deadlinepulse.exe


------------------
管中窥豹: 延伸阅读
------------------
