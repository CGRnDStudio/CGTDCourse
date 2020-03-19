=================================
Houdini流程介绍及渲染代码分析
=================================

Houdini是一款三维计算机图形软件，由加拿大Side Effects Software Inc.（简称SESI）公司开发，SESI公司由Kim Davidson和Greg Hermanovic创建于1987年。Houdini是在Prisms基础上重新开发而来，可运行于Linux, Windows, Mac OS等操作系统，是完全基于节点模式设计的产物，其结构、操作方式等和其它的三维软件有很大的差异。Houdini自带的渲染器是Mantra，基于Reyes渲染架构，因此也能够快速的渲染运动模糊、景深和置换效果。Mantra是经过产品验证的成熟渲染器，可以满足电影级别的渲染要求。当然，Houdini也有第三方渲染器的接口，比如：RenderMan、Mental ray、V-Ray和Torque等，可以把场景导出到这些渲染引擎进行渲染。此部分文档主要用来探讨在Houdini中所有可行的编程方案以及更好的Pipeline解决方案。

----------------------
几种渲染器介绍
----------------------

Mantra
Karma

Arnold
Redshift

V-Ray
RenderMan

------------------------
认识环境变量HOUDINI_PATH
------------------------

环境变量可以让所有扩展插件共存，HOUDINI_PATH。

.. code-block:: bash

    # Redshift env
    RS_PATH = C:/ProgramData/Redshift
    PATH = $PATH;$RS_PATH/bin

    HOUDINI_PATH = $RS_PATH/Plugins/Houdini/18.0.348;&

.. code-block:: bash

    # htoa env
    HTOA = M:/thirdParty/htoa/htoa-5.1.0_r9289183_houdini-18.0.348/htoa-5.1.0_r9289183_houdini-18.0.348
    PATH = $PATH;$HTOA/scripts/bin
    solidangle_LICENSE = 5053@localhost

    # HOUDINI_PATH
    HOUDINI_PATH = $HTOA;&

----------------------
渲染的模式
----------------------

串联与并联的区别

prepost与merge的区别

FrameByFrame与RopByRop区别

.. code-block:: python

    Help on method render in module houpythonportion:

    render(*args, **kwargs) method of hou.RopNode instance
        render(self, frame_range=(), res=(), output_file=None,
        output_format=None, to_flipbook=False, quality=2, ignore_inputs=False,
        method=RopByRop, ignore_bypass_flags=False, ignore_lock_flags=False,
        verbose=False, output_progress=False)

----------------------
后台渲染的三种方案
----------------------

Houdini后台输出一般支持所有的ROP节点，比如：

 - ROP Output Driver(rop_geometry)
 - ROP Alembic Output(rop_alembic)
 - File Cache(filecache)
 - RF Mesh Export(rf_mesh_export)
 - RF Particle Export(rf_particle_export)
 - Mantra(ifd)
 - Arnold(arnold)
 - OpenGL(opengl)
 - Fetch(fetch)
 - Geometry(geometry)
 - Prepost(prepost)
 - Merge(merge)
 - Redshift(Redshift_ROP)

* hbatch | hscript

安装路径bin文件夹下的hscript.exe和hbatch是一样的东西，没有任何区别，正常我们会使用hbatch.exe。

.. code-block:: python

    Usage: hbatch [-R][-e name=value][-c <command>][-j nproc][-h][-i][-q][-v][file.hip ...]

    hbatch shell.  This is the non-graphical interface to a hip
    file.  Type "help" for a list of commands.

    Any number of .hip, .cmd, or .otl files may be specified on the
    command line.  Multiple .hip files are merged together.

    The -e option sets the named enviroment variable to the given
            value.  There should be no spaces around the '=' separator between
            the name and value (i.e. -e foo=bar)

    The -c option will run the option argument as an hscript command, after
            the specified files have been loaded.

    The -f option forces the use of asset definitions found in OTL
            files specified on the command line.

    The -j option sets the HOUDINI_MAXTHREADS to the given value.
    The -h option shows this message
    The -q option prevents the version information from being printed
    The -w option suppresses load warnings and errors from being printed
    The -v option specifies verbose handling of renders
    The -i option uses a simpler interface for reading input
            when running hbatch from other applications (like Pixar's
            Alfred), it may be necessary to use this option.  Use of this
            option will disable several commands (openport and atjob)
    The -R option will request a non-graphics token instead
            of a graphical on

.. code-block:: bash

    hbatch myscene.hip
    Director -> help render
    Director -> render mantra1

.. code-block:: bash

    hbatch
    Director -> mread myscene.hip
    Director -> help render
    Director -> render mantra1

* hrender

hrender是通过csh.exe来调用的，所以得编写csh脚本。

.. code-block:: bash

    Usage:

    Single frame:   hrender    [options] driver|cop file.hip [imagefile]
    Frame range:    hrender -e [options] driver|cop file.hip

    driver|cop:     -c /img/imgnet
                    -c /img/imgnet/cop_name
                    -d output_driver

    options:        -w pixels       Output width
                    -h pixels       Output height
                    -F frame        Single frame
                    -b fraction     Image processing fraction (0.01 to 1.0)
                    -t take         Render a specified take
                    -o output       Output name specification
                    -v              Run in verbose mode
                    -I              Interleaved, hscript render -I

    with "-e":      -f start end    Frame range start and end
                    -i increment    Frame increment

    Notes:  1)  For output name use $F to specify frame number (e.g. -o $F.pic).
            2)  If only one of width (-w) or height (-h) is specified, aspect ratio
                will be maintained based upon aspect ratio of output driver.

批量渲染多个hip文件，将下面文件保存成.csh文件

.. code-block:: bash

    #!C:/PROGRA~1/SIDEEF~1/HOUDIN~1.378/bin/csh.exe -f
    hrender -e -f 1 5 -v -d /obj/ropnet1/mantra1 D:/test/test1.hip
    hrender -e -f 1 10 -v -d /obj/ropnet1/mantra1 D:/test/test2.hip

* hython

自从Houdini引入Python接口之后，逐渐Python成为了HScript的替代品。

.. code-block:: python

    usage: hython [hip_files] [options] ... [-c cmd | -m mod | file | -] [arg] ...
    Extra options supported by hython:
    -b     : enable background openport command processing
    -j arg : sets HOUDINI_MAXTHREADS to the given value;
            arg is the max number of threads

    Regular Python options:
    usage: hython [option] ... [-c cmd | -m mod | file | -] [arg] ...
    Options and arguments (and corresponding environment variables):
    -B     : don't write .py[co] files on import; also PYTHONDONTWRITEBYTECODE=x
    -c cmd : program passed in as string (terminates option list)
    -d     : debug output from parser; also PYTHONDEBUG=x
    -E     : ignore PYTHON* environment variables (such as PYTHONPATH)
    -h     : print this help message and exit (also --help)
    -i     : inspect interactively after running script; forces a prompt even
            if stdin does not appear to be a terminal; also PYTHONINSPECT=x
    -m mod : run library module as a script (terminates option list)
    -O     : optimize generated bytecode slightly; also PYTHONOPTIMIZE=x
    -OO    : remove doc-strings in addition to the -O optimizations
    -R     : use a pseudo-random salt to make hash() values of various types be
            unpredictable between separate invocations of the interpreter, as
            a defense against denial-of-service attacks
    -Q arg : division options: -Qold (default), -Qwarn, -Qwarnall, -Qnew
    -s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
    -S     : don't imply 'import site' on initialization
    -t     : issue warnings about inconsistent tab usage (-tt: issue errors)
    -u     : unbuffered binary stdout and stderr; also PYTHONUNBUFFERED=x
            see man page for details on internal buffering relating to '-u'
    -v     : verbose (trace import statements); also PYTHONVERBOSE=x
            can be supplied multiple times to increase verbosity
    -V     : print the Python version number and exit (also --version)
    -W arg : warning control; arg is action:message:category:module:lineno
            also PYTHONWARNINGS=arg
    -x     : skip first line of source, allowing use of non-Unix forms of #!cmd
    -3     : warn about Python 3.x incompatibilities that 2to3 cannot trivially fix
    file   : program read from script file
    -      : program read from stdin (default; interactive mode if a tty)
    arg ...: arguments passed to program in sys.argv[1:]

    Other environment variables:
    PYTHONSTARTUP: file executed on interactive startup (no default)
    PYTHONPATH   : ';'-separated list of directories prefixed to the
                default module search path.  The result is sys.path.
    PYTHONHOME   : alternate <prefix> directory (or <prefix>;<exec_prefix>).
                The default module search path uses <prefix>\lib.
    PYTHONCASEOK : ignore case in 'import' statements (Windows).
    PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.
    PYTHONHASHSEED: if this variable is set to 'random', the effect is the same
    as specifying the -R option: a random value is used to seed the hashes of
    str, bytes and datetime objects.  It can also be set to an integer
    in the range [0,4294967295] to get hash values with a predictable seed.
    [Redshift]Closing the RS instance. End of the plugin log system.

.. code-block:: bash

    hython myscene.hip
    rnode = hou.node("/out/mantra1")
    help(rnode)
    rnode.render()

.. code-block:: bash

    hython
    import hou
    hou.hipFile.load(myscene.hip)
    rnode = hou.node("/out/mantra1")
    help(rnode)
    rnode.render()

.. code-block:: bash

    hython -c "hou.hipFile.load('hip文件路径'); ropNode = hou.node('输出节点路径'); ropNode.render(frame_range=(1, 10), verbose=True)"
    hython rRop.py

------------------------
认识hou模块
------------------------

hou模块可以分为三大类sub-modules、classes、functions。

* sub-modules：首字母小写，不带括号为module，module可能又有classes以及functions。
* classes：首字母大写，不带括号为class。class必须实例化使用，class的属性以及方法必须通过实例化对象调用。
* functions：首字母小写，带括号为function。

------------------------
参考文档
------------------------

* 《`Rendering as part of a workflow <https://www.sidefx.com/docs/houdini/render/batch.html#hython-and-hbatch>`_》