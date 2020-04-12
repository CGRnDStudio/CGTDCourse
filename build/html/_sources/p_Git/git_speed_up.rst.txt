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

但现在还有一件事情待解决，如果是自建的代码仓库，推送代码到仓库的时候是否会自动同步到Github或者Gitlab呢？

测试一下，



当然想解决自己公司的仓库推送和拉取速度缓慢的问题，可以自己搭建Gitlab本地服务器，云时代我还是比较喜欢用云端产品。



