=========================================
Katana XGen毛发渲染流程
=========================================

解决三个问题。

XGen毛发nHair驱动解算流程？

在制作毛发资产的时候需要通过Guides To Curves转引导曲线，以引导曲线转nHair动力学做毛发解算。

Katana渲染XGen毛发的流程？

这里涉及到环境部署，首先Katana的安装，比较傻瓜式，这里不细说，然后是KTOA（Arnold for Katana）的安装，KTOA可以部署到服务器（也就是共享文件夹中），也是傻瓜式部署，部署完安装路径下有一个launchKtoA.bat的启动项，我们需要稍加修改，才能渲染XGen毛发。内容中MTOA_PATH和MAYA_PATH需要配置，特别是MTOA和KTOA的版本搭配有一定的要求。

.. code-block:: python

    set "KATANA_HOME=C:\Program Files\Katana3.5v2"
    set "KTOA_HOME=%cd%"
    set "MTOA_PATH=\\server\manager\thirdParty\maya\mtoa\3.3.0.1\2017"
    set "MAYA_PATH=C:\Program Files\Autodesk\Maya2017"
    set DEFAULT_RENDERER=arnold
    set "KATANA_TAGLINE=With KtoA 2.4.0.5 and Arnold 5.4.0.3"

    set "path=%KTOA_HOME%\bin;%path%"
    set "KATANA_RESOURCES=%KTOA_HOME%"
    "%KATANA_HOME%\bin\katanaBin.exe"

修改完之后双击bat启动Katana，创建ArnoldXGen节点导入.xgen文件，创建Material（给ambient_occlusion材质），创建MaterialAssign赋予材质，创建相机，RenderSettings以及Render节点就可以渲染出XGen毛发啦。注意的是，XGen毛发在Katana中是无法显示的，只能渲染。

毛发解算完迭代渲染流程？

解算环节输出引导曲线的abc缓存，在Maya中替换驱动毛发，然后通过Export Patches for Batch Render导出.xgen文件即可。

关闭nucleus>Enable，关闭hairSystem>Use Nucleus Solver，改static

Katana本地批量渲染

https://www.aducg.com/2015/07/22/katana-local-batch-rendering-command/


/usr/local/Katana1.5v1/katana --batch --katana-file=/path/to/file/scene.katana --render-node=Render_Node_Name -t 1-20

如何渲染多帧

如何导入相机

如何设置参数

如何随机颜色

.. code-block:: python

    import NodegraphAPI
    from Katana import KatanaFile
    from Katana import RenderManager
    def messageHandler( sequenceID, message ):
        print message

    RenderNode = NodegraphAPI.GetNode('Render') # Getting Render node
    renderSettings = RenderManager.RenderingSettings()
    renderSettings.mode=RenderManager.RenderModes.DISK_RENDER
    renderSettings.asynchRenderMessageCB=messageHandler
    renderSettings.asynch=False
    for frame in range(6, 100):
        print '-' * 80
        print '\nRendering Node "%s" frame %s...' % (RenderNode.getName(), frame)
        renderSettings.frame = frame
        RenderManager.StartRender('diskRender', node=RenderNode, settings=renderSettings)


遇到的坑

- [×] XGen渲染运动模糊需要单独设置
- [×] XGen解算的时候引导曲线（所有的）需要单独导出小数帧给会XGen（-0.1， 0.1），在Katana中只导入.xgen文件，.xgen文件记录了所有缓存路径信息。
- [×] XGen生长面小数帧也不能有任何问题。
- [×] XGen需要单独输出生长面的abc缓存（小数帧）
- [×] XGen生长面和引导曲线的缓存不能脱离，小数帧也不能脱离，不然就会ci掉
