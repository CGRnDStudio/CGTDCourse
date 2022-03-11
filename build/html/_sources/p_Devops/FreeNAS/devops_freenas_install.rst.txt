=========================================
FreeNAS：硬件配置以及系统安装
=========================================

FreeNAS是一套基于FreeBSD操作系统核心的开放源代码的网络存储设备（NAS）服务器系统，支持众多服务，用户访问权限管理，提供网页设置接口。

硬件配置：

- R730XD E5 2678v3*2 32G*4 8T*12 H330阵列卡 x710四口万兆网卡

因为没有配置SSD固态盘作为系统盘，FreeNAS使用软RAID，所以不通过BIOS来配置硬盘的RAID，我们先做系统，为了将操作系统和存储数据分开，准备两个U盘，如果你有专门固态盘作为系统盘的话只需要一个U盘，将系统做到SSD中即可，这里我选择将系统做到另一个U盘中。这里我将FreeNAS做到32G的U盘中。

随便找台win电脑，将FreeNAS镜像烧录到其中一个U盘。需要下载两个东西。

- win32diskimager-1.0.0-install.exe
- FreeNAS-11.3-RELEASE.iso

一旦烧录了FreeNAS操作系统，U盘将不在盘符区显示，如果需要重新烧录，你会发现U盘无法格式化，推荐你们使用DiskGenius工具格式化分区，非常好用。

开机按F2配置BIOS启动（去掉UEFI如果设置过），重启按F11选择U盘启动。


- [ ] 测试U盘恢复FreeNAS系统
- [ ] FreeNAS域环境配置
- [ ] 测试FreeNAS读写速度
- [ ] FreeNAS软RAID
- [√] FreeNAS共享文件
- [ ] FreeNAS文件系统怎么用
- [ ] FreeNAS配置备份，如何一键恢复
- [√] FreeNAS如何固定IP
- [√] FreeNAS权限管理
- [ ] FreeNAS软链接是否可用

FreeNAS设置静态IP，在Web端选择Network>Interfaces，找到对应的网卡，比如bge1，DHCP自动分配去勾选，设置IP Address。

FreeNAS创建用户以及用户权限。


---------------------------
参考文档
---------------------------


- https://www.getnas.com/freenas-installation/
- https://blog.csdn.net/sanwe3333/article/details/104831493
- http://www.freenas.com.cn/
- https://www.getnas.com/freenas-static-ip/
- https://www.cnblogs.com/hjc4025/p/7079364.html
