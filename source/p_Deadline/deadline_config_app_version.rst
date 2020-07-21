=============================
Deadline渲染农场配置软件版本
=============================

配置软件版本需要配置两个地方，首先如果你是使用默认菜单提交方式，想添加软件版本可以通过修改下面的模块文件

.. code-block:: python

    DeadlineRepository10\scripts\Submission\HoudiniSubmission.py

此时我们只是能提交我们配置的软件版本，但任务肯定会报错，因为我们还需要配置插件，也就是后台会去调用什么软件版本去跑任务。这里需要去明确配置。

.. code-block:: python

    DeadlineRepository10\plugins\Houdini\Houdini.param
