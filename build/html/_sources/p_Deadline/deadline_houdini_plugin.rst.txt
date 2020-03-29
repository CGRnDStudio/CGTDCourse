===============================
Deadline渲染农场Houdini提交工具
===============================

- 案例：编写Houdini、Nuke提交工具

- Deadline Python API
- 其它CG软件的提交代码
- 其它农场提交代码

.. code-block:: python

    import sys
    sys.path.insert(0, r"Y:\Program\DeadlineRepository10\api\python")
    from Deadline.DeadlineConnect import DeadlineCon as Connect
    con = Connect("farm.do-vfx.com", 8082)
    
    job = con.Jobs.GetJob("5bfce04f4096fe78c0f6d640")
    
    print(job)
    import Deadline.DeadlineConnect as Connect

    Deadline = Connect.DeadlineCon('farm.do-vfx.com', 8082)
    print(Deadline)
    JobInfo = {
        "Name": "Submitted via Python",
        "UserName": "huweiguo",
        "Frames": "1-24",
        "Plugin": "Houdini"
        }
    
    PluginInfo = {
        "OutputDriver": "/obj/ropnet1/mantra1",
        "SceneFile": "Y:/shotTest/untitled.hip",
        "Version": "17.0"
        }
    
    try:
        newJob = Deadline.Jobs.SubmitJob(JobInfo, PluginInfo)
        print newJob
    except:
        print "Sorry, Web Service is currently down!"

Houdini提交工具

- Python API提交任务
- PySide2构建UI界面

Nuke提交工具

- Python API提交任务
- PySide2构建UI界面
