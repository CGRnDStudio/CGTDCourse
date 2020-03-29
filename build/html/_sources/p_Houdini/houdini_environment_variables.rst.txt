==============================
Houdini中心化理念：环境变量
==============================

Houdini中心化理念又称集成式环境部署，中心化最重要的知识点就是环境变量，HOUDINI_PATH在Houdini中是及其重要的一个环境变量，它管控Houdini扩展开发插件的层级结构。

打开菜单Windows>Shell，输入hconfig -ap可以获取Houdini中所有环境变量的用途描述，第一个就是HOUDINI_PATH。

.. code-block:: bash

    C:\Users\huweiguo>hconfig -ap
    Common paths are set to:
    $JOB = C:/Users/huweiguo
    $HIP = C:/Users/huweiguo
    $HOUDINI_USER_PREF_DIR = C:/Users/huweiguo/Documents/houdini16.5
    $HOME = C:/Users/huweiguo/Documents
    $HSITE = C:/PROGRA~1/SIDEEF~1/HOUDIN~1.378/site
    $HFS = C:/PROGRA~1/SIDEEF~1/HOUDIN~1.378

    HOUDINI_PATH := ""
        The path of directories where Houdini looks for configuration files.

        Directories searched (in order) are:
            1) "$HIP"
            2) "$HOUDINI_USER_PREF_DIR"
            3) "$HFS/houdini"
            4) "$HFS/bin"

在Houdini中想扩展开发插件，插件的层级结构可参考"$HFS/houdini"，$HFS是Houdini安装所在的路径。

- config/Icons # 自定义图标
- desktop # 自定义布局
- dso # 自定义HDK C++编译的插件
- gallery # 自定义节点预设
- geo # 自定义一些bgeo缓存
- ocio # 自定义色彩空间
- otls # 自定义otl文件
- presets # 自定义节点参数预设
- python_panels # 自定义Python面板
- radialmenu # 自定义热盒菜单
- scripts/python # 自定义Python代码可以放这
- toolbar # 自定义工具架工具
- FBres # 自定义分辨率预设
- MainMenuCommon.xml # 自定义主菜单
- OPmenu.xml # 自定义节点右键菜单
- PARMmenu.xml # 自定义节点参数右键菜单
- VEXpressions.txt # 自定义VEX代码片段

还有很多其它可以自定义的配置文件，可以详细研究一下。


坐井观天：本节知识点
认识环境变量HOUDINI_PATH
如何部署qLib
Shell & hconfig
houdini.env
.bat批处理文件管理环境变量 伪装快捷方式
集中式管理Arnold，Redshift，V-Ray，Renderman，RFConnect，Denoiser等
集中式管理插件的好处，方便维护，方便版本切换
几种常用的环境变量



管中窥豹：延伸阅读
http://127.0.0.1:48626/basics/config_env
http://127.0.0.1:48626/ref/env.html
https://github.com/qLab/qLib
https://docs.chaosgroup.com/display/VRAYHOUDINI/QuickStart+Guides



Shell

hconfig
hconfig -a
hconfig -ap
set 某个环境变量


几种常用的环境变量
HOUDINI_BUFFEREDSAVE 加速Houdini网盘文件存储
HOUDINI_ACCESS_METHOD 控制abc, hip文件无权限读取
HOUDINI_EXTERNAL_HELP_BROWSER 设置默认谷歌浏览器打开帮助文档
HOUDINI_OTLSCAN_PATH
HOUDINI_SPLASH_FILE 修改启动图片

Arnold
4.0.2\htoa-4.0.2_r236e192_houdini-17.5.229

# Arnold env
HTOA = //server/manager/thirdParty/tools/htoa/4.0.2/htoa-4.0.2_r236e192_houdini-17.5.229
PATH = $PATH;$HTOA/scripts/bin
solidangle_LICENSE = 5053@farm.do-vfx.com
 
# HOUDINI_PATH
HOUDINI_PATH = $HTOA;&

Redshift\Plugins\Houdini\16.5.268

# Redshift env
RS_PATH = C:/ProgramData/Redshift
PATH = $PATH;$RS_PATH/bin
 
# HOUDINI_PATH
HOUDINI_PATH = $RS_PATH/Plugins/Houdini/16.5.268;&

Pixar\RenderManForHoudini-22.5\17.5

# RenderMan env
RMAN = C:/Program Files/Pixar
RMANTREE = $RMAN/RenderManProServer-22.5
RFHTREE = $RMAN/RenderManForHoudini-22.5
 
# HOUDINI_PATH
HOUDINI_PATH = $RFHTREE/17.5;&

vray\vfh_home


# V-Ray env
VFH_ROOT="//server/manager/thirdParty/tools/vray"
VRAY_APPSDK="$VFH_ROOT/appsdk"
VRAY_OSL_PATH="$VRAY_APPSDK/bin"
VRAY_UI_DS_PATH="$VFH_ROOT/ui"
VFH_HOME="$VFH_ROOT/vfh_home"
VFH_PATH="$VFH_HOME/bin;$VRAY_APPSDK/bin"
PATH="$VFH_PATH;$PATH"
 
# HOUDINI_PATH
HOUDINI_PATH = $VFH_HOME;&
