=========================================
FreeNAS：回收站无权访问刷新ACL控制列表
=========================================

FreeNAS配置的回收站.recycle文件夹时间久了不知道为什么权限就消失了，无法访问别人删除的文件

此时进FreeNAS网页端，找到共享>Windows共享（SMB）>编辑访问控制列表>递归应用权限>将权限应用于子数据集>保存就行