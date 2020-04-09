=========================================
Squid代理服务器搭建
=========================================

VMware部署一台CentOS7 Linux虚拟机。

.. code-block:: bash

    # 安装
    yum install squid -y
    yum install httpd-tools -y
    # 服务启动
    systemctl start squid.service
    # 服务停止
    systemctl stop squid.service
    # 配置开机自启动
    systemctl enable squid.service
    # 服务重启
    systemctl restart squid.service
    # 关闭防火墙
    systemctl stop firewalld.service
    # 禁用防火墙
    systemctl disable firewalld.service