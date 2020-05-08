================================
Nuke Python命令行传参的两种方案
================================

后台调用Nuke的Python执行环境有两种方案，打开命令行窗口，下面的两句脚本都是可以打开Nuke的Python执行环境。

.. code-block:: python

    "C:\Program Files\Nuke10.5v1\python.exe" blablabla.py arg1 arg2 arg3
    "C:\Program Files\Nuke10.5v1\Nuke10.5.exe" -t blablabla.py arg1 arg2 arg3

命令行窗口给py文件传参也有两种方案，一种最普通的方式通过sys.argv来获取参数，但是在两种执行环境中都有一些问题，第一种执行环境下blablabla.py文件中import nuke和sys.argv得有先后顺序。

.. code-block:: python

    import sys
    print(sys.argv)

    import nuke
    print(nuke.__file__)

上面的代码是可以正常传递命令行参数的，但下面这种情况就不行，你会得到空列表。

.. code-block:: python

    import sys
    import nuke

    print(sys.argv)
    print(nuke.__file__)

第二种执行环境下不存在这样的问题，但是对于数字型的参数，它会遇到警告，这种参数通过sys.argv存储不了。比如：

.. code-block:: python

    "C:\Program Files\Nuke10.5v1\Nuke10.5.exe" -t blablabla.py 101 200

**WARNING: The command line argument ' 101 200' will be used as a Frame Range argument and will not be forward to the python sys.argv.
To define a frame range argument use the -F option.**


此时可以通过nuke.rawArgs来获取就是OK的。
