================================
Deadline渲染农场MongoDB离线安装
================================

在安装DeadlineRepository的时候，会遇到在线安装MongoDB数据库服务器的需求，如果在线下载安装往往非常非常慢，无法忍受。

在Deadline官方安装文档中有提到可以先下载MongoDB数据库服务器离线安装包，再来安装，这样速度是极快的。

Deadline 10.1版本所要求的MongoDB版本在3.2.12~3.6.16之间。

上MongoDB官网 https://www.mongodb.com/download-center 下载，找到Server选项，选择配置，我这里拿Windows 10操作系统做的测试，稳定性考虑建议使用服务器操作系统，将Deadline搭建在服务器上，比如Windows Server 2012 R2 Standard，下面的配置是测试配置按实际环境修改。

- Version: 3.4.24(previous release)
- OS: Windows x64
- Package: ZIP

我这里下下来是这样一个安装包mongodb-win32-x86_64-2008plus-ssl-3.4.24.zip，在安装DeadlineRepository选择这个离线安装包安装就可以了。

参考文档：

- https://docs.thinkboxsoftware.com/products/deadline/10.1/1_User%20Manual/manual/install-db-repo.html