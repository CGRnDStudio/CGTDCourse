=============================
Houdini
=============================

Houdini是一款三维计算机图形软件，由加拿大Side Effects Software Inc.（简称SESI）公司开发，SESI公司由Kim Davidson和Greg Hermanovic创建于1987年。Houdini是在Prisms基础上重新开发而来，可运行于Linux, Windows, Mac OS等操作系统，是完全基于节点模式设计的产物，其结构、操作方式等和其它的三维软件有很大的差异。Houdini自带的渲染器是Mantra，基于Reyes渲染架构，因此也能够快速的渲染运动模糊、景深和置换效果。Mantra是经过产品验证的成熟渲染器，可以满足电影级别的渲染要求。当然，Houdini也有第三方渲染器的接口，比如：RenderMan、Mental ray、V-Ray和Torque等，可以把场景导出到这些渲染引擎进行渲染。此部分文档主要用来探讨在Houdini中所有可行的编程方案以及更好的Pipeline解决方案。

Contents:

.. toctree::
   :maxdepth: 1
   :glob:

   ../p_Houdini/houdini_environment_variables
   ../p_Houdini/houdini_custom_menu