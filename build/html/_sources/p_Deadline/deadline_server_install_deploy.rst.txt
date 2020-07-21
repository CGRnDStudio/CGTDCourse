==============================
Deadline渲染农场服务器安装部署
==============================

文档采用服务器集中式部署方案，将DeadlineRepository与DeadlineClient全部部署在服务器，从而客户端无需安装任何东西即可使用的方案。

部署环境如下:

- 服务器：Windows Server 2012 R2 Standard
- 客户端：Window 10 企业版
- Deadline版本：Thinkbox Deadline v10.0.20.2 Win

远程控制，需要开启deadlinepulse.exe

Deadline如果使用服务器部署存在三个问题需要解决，一个是安装的路径得是共享路径，在D盘你是没法在另一台电脑上开启客户端软件连接数据库的。客户端电脑有时候打不开Deadline的原因可能是需要安装.net的库，一般安装完Maya就可以解决这个问题。还有会遇到deadline.ini文件找不到的问题，可以直接拷贝Thinkbox\Deadline10\bin\Thinkbox\Deadline10\deadline.ini文件到下面的路径中。

.. code-block:: python

    C:\ProgramData\Thinkbox\Deadline10
