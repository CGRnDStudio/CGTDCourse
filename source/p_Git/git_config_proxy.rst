==============================
Git配置代理网络访问
==============================

首先我们要用Vmware+CentOS搭建一个代理服务器，比如IP是192.168.0.112。

内网Git可以通过配置代理访问远程仓库。

.. code-block:: python

    git config --global http.proxy 192.168.0.112:3128

如果内网搭建了域以及DNS服务器做了IP映射，也可以通过下面的方式来配置。

.. code-block:: python

    git config --global http.proxy squid.do-vfx.com:3128

如果不想使用代理服务器了，可以使用下面的指令移除配置。

.. code-block:: python

    git config --global --unset https.proxy
