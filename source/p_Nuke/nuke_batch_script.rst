==============================
Nuke执行后台命令脚本方案
==============================


两种后台命令脚本的模式

打开命令行可以通过标签-h或者--help查询帮助
"C:\Program Files\Nuke10.5v1\Nuke10.5.exe" -h

基本语法

./Nuke (--nukex) <switches> <script> <argv>

<switches> 标签flag
<script> .nk文件的路径
<argv> 传入的参数可以中.nk文件中以[arg n]来使用

简单的案例
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" "D:/test.nk"
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" --nukex "D:/test.nk"
直接跟.nk文件，表示打开这个合成文件

"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" -x -F 1-80 -X Write1 -m 8 --cont "D:/test.nk"
标签-x 将.nk文件输出
标签-F起始帧-结束帧
标签-X 输出节点名称
标签-m 设置线程数，默认占用电脑所有线程
标签--cont 渲染出错继续

命令行输出多个Write，创建一个txt文件，将扩展名改为bat，内容写入
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" -x -F 1-80 -X Write1 -m 8 --cont "D:/test.nk"
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" -x -F 1-80 -X Write2 -m 8 --cont "D:/test.nk"
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" -x -F 1-80 -X Write3 -m 8 --cont "D:/test.nk"

写个渲染完自动关机的bat，加shutdown关机命令
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" -x -F 1-80 -X Write1 -m 8 --cont "D:/test.nk"
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" -x -F 1-80 -X Write2 -m 8 --cont "D:/test.nk"
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" -x -F 1-80 -X Write3 -m 8 --cont "D:/test.nk"
shutdown /f /s

-F range的三种写法：A、A-B、A-BxC


标签-t后面可以跟.py文件，案例
"C:/Program Files/Nuke10.5v1/Nuke10.5.exe" -t "W:/houdini/scripts/python/slateMov/nkSlate.py"

另一种方案是通过
"C:/Program Files/Nuke10.5v1/python.exe" "W:/houdini/scripts/python/slateMov/nkSlate.py"

.py文件一般有两种写法，一种是通过代码生成或读取.nk模板文件输出，另一种是不生成nk文件直接输出

分块合并的原理一般来说是几张图通过Read节点读入，然后连接不同的transform节点（注意transform参数需要按具体几张图来设置），最后通过merge节点将分块的图缝合拼接，再接Write节点输出一整张图（注意nuke不认中文或特殊字符的文件路径）

比如一张2500x1250的图被分16块，(156x1250x15张+160x1250x1张)
渲染出了16张图，在Nuke中先创建一个2500宽x1250高的constant
然后将16张图依次和constant背景merge中一起输出

算好每个transform的水平位置的平移值



subprocess模块进程通信
subprocess.Popen类初始化
__init__(self, args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
创建并返回一个子进程，并在这个进程中执行指定的程序。
　　实例化 Popen 可以通过许多参数详细定制子进程的环境，但是只有一个参数是必须的，即位置参数 args ，下面也会详细介绍剩余的具名参数。
args：要执行的命令或可执行文件的路径。一个由字符串组成的序列（通常是列表），列表的第一个元素是可执行程序的路径，剩下的是传给这个程序的参数，如果没有要传给这个程序的参数，args 参数可以仅仅是一个字符串。
 
案例

.. code-block:: python

    import subprocess
    # Start Houdini
    subprocess.Popen("C:/Program Files/Side Effects Software/Houdini 16.5.378/bin/houdinifx.exe")
    # Start Nuke
    subprocess.Popen("C:/Program Files/Nuke10.5v1/Nuke10.5.exe")
    # Start NukeX
    subprocess.Popen("'C:/Program Files/Nuke10.5v1/Nuke10.5.exe' -nukex")
    # Start Nukex
    subprocess.Popen(["C:/Program Files/Nuke10.5v1/Nuke10.5.exe", "-nukex"])
    # Nuke Write
    subprocess.Popen(["C:/Program Files/Nuke10.5v1/Nuke10.5.exe", "-nukex -x -F 1", "A:/working/101011621/b34dfc17-6395-4150-b310-7761074d26b6/Bin/tmp/7712/tmp370147.tga.nk", "D:/2019/aaa/test.exr"])
    # Python Write
    subprocess.Popen(["C:/Program Files/Nuke10.5v1/Nuke10.5.exe", "-nukex", "-t", "D:/2019/aaa/test.py", "A:/working/101011621/b34dfc17-6395-4150-b310-7761074d26b6/Bin/tmp/7712/Tile", "D:/2019/aaa/test.exr"])
    # subprocess.Popen(["C:/Program Files/Nuke10.5v1/python.exe", pyModule, nkPath, movPath, fileStepName, reviewPath, USER, ext])

    # nuke.scriptOpen(nk)

.. code-block:: python

    # test.py

    import os
    import re
    import sys
    import nuke

    # print(sys.argv)

    def abortSelected():
        return [i['selected'].setValue(False) for i in nuke.allNodes()]

    abortSelected()
    mergeNode = nuke.createNode("Merge2", inpanel=False)
    abortSelected()
    writeNode = nuke.createNode("Write", inpanel=False)
    writeNode.setInput(0, mergeNode)
    writeNode["file"].setValue(sys.argv[2])
    abortSelected()
    consNode = nuke.createNode("Constant", inpanel=False)
    nuke.addFormat("%s %s %s" % (2500, 1250, "newRes"))
    consNode["format"].setValue("newRes")

    mergeNode.setInput(0, consNode)


    def sort_item(item):
        return int(re.search(r"(?<=__1x)\d+", item).group())

    tempWidth = 0
    for elem in sorted(os.listdir(sys.argv[1]), key=sort_item):
        # print(elem)
        i = sort_item(elem)
        print(i)
        res_check = re.search(r'(?<=__)\d+x\d+_[Ww]\d+[Hh]\d+(?=__.)', elem)
        cur_Width = re.search(r'(?<=_[Ww])\d+(?=[Hh])', res_check.group())
        cur_Height = re.search(r'(?<=[Hh])\d+$', res_check.group())
        # print(res_check.group())
        # print(cur_Width.group())
        # print(cur_Height.group())

        readNode = nuke.nodes.Read()
        readNode["file"].fromUserText(sys.argv[1] + "/" + elem)
        abortSelected()
        tranNode = nuke.createNode("Transform", inpanel=False)
        # print(tempWidth)
        tranNode.knob("translate").setValue((tempWidth, 0))

        tranNode.setInput(0, readNode)
        print(tranNode.name())
        mergeNode.setInput(i+2, tranNode)

        tempWidth += int(cur_Width.group())

    # nuke.scriptSave("D:/2019/aaa/test.nk")
    nuke.execute(writeNode, 1, 1, 1)
