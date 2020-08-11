=============================
PyQt VS PySide
=============================

PyQt是GPLv3协议，大意是你的程序中用了它，你的程序就要开源，如果闭源商用就会违反协议（后果自负，脸皮够厚无所谓）。除非你搞封装动态加载那一套来强行规避。

PySide是LGPL协议，如果你只是作为库用用它，你的程序还是可以闭源商用。

所以很多人喜欢PySide。如果不做商业项目，强烈建议使用PyQt，资料多，稳定。需要开发闭源商用软件的就用PySide。

GPL(General Public License)和LGPL( Lesser General Public License)是GNU的两种License。越来越多的自由软件(Free Software)使用GPL作为其授权声明，如果对GPL一点都不了解，有可能在使用自由软件时违反了GPL的授权。如果是个人或不正规的公司倒也无所谓，但如果是有规模的公司，恐怕会有被起诉的风险。

LGPL是GPL的变种，也是GNU为了得到更多的甚至是商用软件开发商的支持而提出的。与 GPL的最大不同是，可以私有使用LGPL授权的自由软件，开发出来的新软件可以是私有的而不需要是自由软件。所以任何公司在使用自由软件之前应该保证在 LGPL或其它GPL变种的授权下。

pyside2-uic.exe VS pyuic5.exe

pyside2-rcc.exe VS pyrcc5.exe

pyqtSignal VS Signal

pyqtSlot VS Slot

- https://blog.csdn.net/The_Time_Runner/article/details/89329556
- https://wiki.qt.io/Differences_Between_PySide_and_PyQt/zh
- https://www.zhihu.com/question/21237276
- https://maicss.gitbooks.io/pyqt5/content/%E4%BA%8B%E4%BB%B6%E5%92%8C%E4%BF%A1%E5%8F%B7.html
