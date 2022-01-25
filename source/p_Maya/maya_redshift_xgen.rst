================================
Maya Redshift渲染Xgen毛发流程
================================

- 创建个球和地面，选择球Import Preset From Library，选择Sheep预设

- 创建Redshift Physical Light，修改Light Type>Directional，Intensity Multiplier>1

- 创建Redshift Dome Light，降低Tint

- 创建RedshiftHair材质，选择description给上材质

- 修改Xgen面板Renderer为Redshift

- 修改Render Settings>GI>Brute Force，采样32-128

- 创建RedshiftUserDataColor节点连接到rsHair节点

.. image:: rshair.png

.. image:: xgen_hair1.png

- 实现颜色过度，创建RedshiftHairPosition和ramp[Texture]节点连接

.. image:: rsramp.png

.. image:: xgen_hair2.png


