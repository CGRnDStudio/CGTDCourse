=============================
Deadline渲染农场提交农场接口
=============================

文档采用服务器集中式部署方案，将DeadlineRepository与DeadlineClient全部部署在服务器，从而客户端无需安装任何东西即可使用的方案。

部署环境如下:

* 服务器：Windows Server 2012 R2 Standard
* 客户端：Window 10 企业版
* Deadline版本：Thinkbox Deadline v10.0.20.2 Win



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

## Deadline客户端电脑配置
- C:\ProgramData\Thinkbox\Deadline10 deadline.ini

## Deadline使用与配置
- Deadline软件界面
- Deadline使用方法
- Deadline简单配置

# 坐井观天：本节知识点
- 案例：编写Houdini、Nuke提交工具



------------------
管中窥豹: 延伸阅读
------------------
