==============================
Git国外服务器加速方案
==============================

不管是Github还是Gitlab都是国外服务器托管代码的平台，这就导致了代码推送或者拉取的时候速度受到限制。

那么如何曲线救国呢？

咱以一个开源仓库qLib下载作为测试案例。

.. code-block:: python

    git clone https://github.com/qLab/qLib

500M移动网络拉取代码速度只有30~50kb左右，代码仓库小还没什么影响，一旦文件过多基本以失败告终。

上国内代码托管平台码云注册账号，创建仓库的时候选择从Gitlab/Github导入仓库。

选择从URL导入，填写代码仓库网址。

.. code-block:: python

    https://github.com/qLab/qLib.git


再次尝试拉取仓库，此次使用码云仓库链接，速度变成10M/s，100M的仓库10s就下载完成啦，牛逼！

.. code-block:: python

    git clone https://gitee.com/CGRnDStudio/qLib.git

此时的码云仓库和国外平台仓库一毛钱关系没有，如果国外平台仓库更新了，需要手动同步才能将更新的部分同步到码云。

那么如何将自建的代码仓库用码云管理的同时，推送代码的时候能自动同步到Github或者Gitlab呢？

如果你选择码云管理代码仓库，而不需要国外平台，就不没有同步一说。我个人喜欢用Gitlab，所以想通过Gitee来中转。

这里给一个解决方案，git remote多配置一个远程仓库，在push的时候可以同时推送代码到码云和Gitlab上，而拉取代码依然是码云仓库。

.. code-block:: bash

    git remote set-url --add --push origin https://gitee.com/CGRnDStudio/blablabla.git
    git remote set-url --add --push origin https://github.com/CGRnDStudio/blablabla.git

完事之后可以看到.git/config文件中已添加了Github地址。

但我相信应该有更好的解决方案，比如配置webhook技术，还没有去测试，。

当然想解决自己公司的仓库推送和拉取速度缓慢的问题，可以自己搭建Gitlab本地服务器，云时代我还是比较喜欢用云端产品。
