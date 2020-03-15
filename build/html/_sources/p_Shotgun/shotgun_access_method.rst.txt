=============================
Shotgun API访问的两种方式
=============================

------------------
用户名
------------------

管理员用户登陆找到People entity，记住两个字段值Login和Password。

.. code-block:: python

    sg = shotgun_api3.Shotgun("https://do-vfx.shotgunstudio.com",
                              login="字段Login值",
                              password="字段Password值")
    sg.find("Shot", filters=[["sg_status_list", "is", "ip"]], fields=["code", "sg_status_list"])

------------------
Scripts
------------------

管理员用户登陆找到Scripts entity，通过Add Script添加一条Script，记住两个字段值Script Name和Application Key。

.. code-block:: python

    sg = shotgun_api3.Shotgun("https://do-vfx.shotgunstudio.com",
                              login="字段Script Name值",
                              password="字段Application Key值")
    sg.find("Shot", filters=[["sg_status_list", "is", "ip"]], fields=["code", "sg_status_list"])


------------------
参考文档
------------------

《`Shotgun开发人员文档 <https://developer.shotgunsoftware.com/>`_》
《`Shotgun python-api <https://developer.shotgunsoftware.com/python-api/>`_》
