=========================================
Katana配置本地离线帮助文档
=========================================

非常有用的小功能，默认Katana菜单Help中的帮助文档都是链接到在线文档，虽然在线文档可能是访问最新版本文档，但很多时候限于网速原因以及大多时候不能上网的局限，需要配置本地离线帮助文档，查看当前版本的帮助文档。

找到主菜单Edit>Perferences>documentation将source从Remote(via learn.foundry.com)配置成Local即可，此时查看Online Help、Developer Guide以及API Reference都是本地离线帮助文档了，玩API特别方便吧。

NukeX本地离线帮助文档会遇到一点问题，虽然NukeX菜单Edit>Preferences...>Behaviors>Documentation中也有设置documentation source为local的选项，但是设置和不设置好像是一样的，我们只能魔改本地index.html文件了。以Nuke 12.1v2为例，找到C:\Program Files\Nuke12.1v2\Documentation\index.html文件，用记事本打开。

.. code-block:: python

    <!doctype html public "-//w3c//dtd html 4.0 transitional//en">
    <html>
    <head>
    <title>
        Nuke 12.1.2
    </title>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <link href="img/visionmongers.css" rel="stylesheet" type="text/css">
    </head>
    <body>
    <h1>
        <img src="img/nuke.png" alt="[Nuke Logo]">
    </h1>
    <blockquote>
        <p>
        Nuke is an Academy Award winning compositor.
        It has been used to create extraordinary images on scores of
        feature films including <em>Avatar</em>, <em>Harry Potter And The Deathly Hallows</em>,
        <em>Tron: Legacy</em>, <em>Super 8</em> and <em>The Curious Case Of Benjamin Button</em>
        as well as countless commercials and music videos.
        The following
        links take you to Nuke user documentation in various forms,
        here you'll find answers to your questions, whether you're
        a beginner, an experienced Nuke user or a Nuke developer.
        </p>

        <h3>Links</h3>

        <p>
        <b>
            <a href="https://www.foundry.com/products/nuke/online-help">Nuke User Guide Tutorial Resources</a>
        </b> - A link to the Tutorial resources used in the Nuke User Guide.
        (These can be located on our website on the Support > User guides page.).
        </p>
        <p>
        <b>
            <a href="http://learn.foundry.com/nuke/12.1/">Foundry Online Help</a>
        </b> - The Foundry online help for Nuke.
        </p>
        <p>
        <b>
            <a href="http://docs.thefoundry.co.uk/nuke/12.1/pythondevguide/">Nuke Python Developers Guide</a>
        </b> - HTML documentation for Nuke Python developers.
        </p>
        <p>
        <b>
            <a href="http://docs.thefoundry.co.uk/hiero/12.1/hieropythondevguide/">Hiero Python Developers Guide</a>
        </b> - HTML documentation for Hiero Python developers.
        </p>
        <p>
        <b>
            <a href="http://docs.thefoundry.co.uk/nuke/12.1/pythonreference/">Python Scripting Reference</a>
        </b> - An HTML reference for all of Nuke's Python methods and types.
        </p>
        <p>
        <b><a href="Tcl/index.html">TCL Scripting</a></b> - An HTML resource for TCL scripting.
        </p>
        <p>
        <b>
            <a href="Tcl/group__tcl__expressions.html">Knob Math Expressions</a>
        </b> - An HTML list of functions you can use in Nuke expressions.
        </p>
        <p>
        <b>
            <a href="NDKExamples/index.html">C++ Plug-in Development</a>
        </b> - A link to Nuke Developer Kit (NDK) resources.
        </p>
        <p>
        <b>
            <a href="http://docs.thefoundry.co.uk/nuke/12.1/BlinkKernels/">Guide to Writing Blink Kernels</a>
        </b> - An HTML guide for users of the BlinkScript node in Nuke.
        </p>
    </blockquote>
    <br>
    <hr>
        <table width="100%"  border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td>
            <span class="legal">
                &copy;2020 The Foundry Visionmongers, Ltd.  All Rights Reserved.
            </span></td>
            <td>
            <div align="right">
                <span class="legal">
                <a href="http://www.foundry.com" target="_blank">www.foundry.com</a>
                </span>
            </div>
            </td>
        </tr>
        </table>
    </body>
    </html>


直接修改链接的网址路径，像下面这样。

.. code-block:: python

    <!doctype html public "-//w3c//dtd html 4.0 transitional//en">
    <html>
    <head>
    <title>
        Nuke 12.1.2
    </title>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <link href="img/visionmongers.css" rel="stylesheet" type="text/css">
    </head>
    <body>
    <h1>
        <img src="img/nuke.png" alt="[Nuke Logo]">
    </h1>
    <blockquote>
        <p>
        Nuke is an Academy Award winning compositor.
        It has been used to create extraordinary images on scores of
        feature films including <em>Avatar</em>, <em>Harry Potter And The Deathly Hallows</em>,
        <em>Tron: Legacy</em>, <em>Super 8</em> and <em>The Curious Case Of Benjamin Button</em>
        as well as countless commercials and music videos.
        The following
        links take you to Nuke user documentation in various forms,
        here you'll find answers to your questions, whether you're
        a beginner, an experienced Nuke user or a Nuke developer.
        </p>

        <h3>Links</h3>

        <p>
        <b>
            <a href="https://www.foundry.com/products/nuke/online-help">Nuke User Guide Tutorial Resources</a>
        </b> - A link to the Tutorial resources used in the Nuke User Guide.
        (These can be located on our website on the Support > User guides page.).
        </p>
        <p>
        <b>
            <a href="html/content/learn_nuke.html">Foundry Online Help</a>
        </b> - The Foundry online help for Nuke.
        </p>
        <p>
        <b>
            <a href="PythonDevGuide/Nuke/index.html">Nuke Python Developers Guide</a>
        </b> - HTML documentation for Nuke Python developers.
        </p>
        <p>
        <b>
            <a href="PythonDevGuide/Hiero/index.html">Hiero Python Developers Guide</a>
        </b> - HTML documentation for Hiero Python developers.
        </p>
        <p>
        <b>
            <a href="PythonReference/index.html">Python Scripting Reference</a>
        </b> - An HTML reference for all of Nuke's Python methods and types.
        </p>
        <p>
        <b><a href="Tcl/index.html">TCL Scripting</a></b> - An HTML resource for TCL scripting.
        </p>
        <p>
        <b>
            <a href="Tcl/group__tcl__expressions.html">Knob Math Expressions</a>
        </b> - An HTML list of functions you can use in Nuke expressions.
        </p>
        <p>
        <b>
            <a href="NDKExamples/index.html">C++ Plug-in Development</a>
        </b> - A link to Nuke Developer Kit (NDK) resources.
        </p>
        <p>
        <b>
            <a href="Blink/index.html">Guide to Writing Blink Kernels</a>
        </b> - An HTML guide for users of the BlinkScript node in Nuke.
        </p>
    </blockquote>
    <br>
    <hr>
        <table width="100%"  border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td>
            <span class="legal">
                &copy;2020 The Foundry Visionmongers, Ltd.  All Rights Reserved.
            </span></td>
            <td>
            <div align="right">
                <span class="legal">
                <a href="http://www.foundry.com" target="_blank">www.foundry.com</a>
                </span>
            </div>
            </td>
        </tr>
        </table>
    </body>
    </html>

重启NukeX，选择菜单Help>Documentation，就可以直接查看本地的离线帮助文档了，美滋滋，美中不足的是还有一部分链接是在线链接，但大部分都是OK的，也无关紧要。
