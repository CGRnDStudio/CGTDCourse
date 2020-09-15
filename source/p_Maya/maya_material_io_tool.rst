==============================
Maya材质导入导出工具
==============================

.. code-block:: python

    # 获取所有shading group
    cmds.ls(type="shadingEngine")
    # 获取选择物体的shape
    cmds.listRelatives(geo, children=True, path=True)
    cmds.listConnections(shp, destination=True, t="shadingEngine")
    cmds.file(file_path, options="v=0;", typ="mayaAscii", pr=True, es=True)
    cmds.sets(sg, q=True)
    # reference
    cmds.file(file_path, r=True, ns=name_space)
    cmds.sets(filter_items, e=True, forceElement=sg)

.. code-block:: python

    #! /usr/bin/env python
    # -*- coding: utf-8 -*-

    import os
    import json

    import maya.cmds as cmds


    def get_all_sg_nodes():
        """
        获取所有的sg类型的节点
        """
        sg_nodes = cmds.ls(typ="shadingEngine")
        return sg_nodes


    def get_sel_sg_nodes():
        """
        获取所选择物体链接的sg节点
        """
        sg_nodes = list()
        selected_geos = cmds.ls(sl=True)
        for geo in selected_geos:
            shapes = cmds.listRelatives(geo, children=True, path=True) or list()
            for shp in shapes:
                sg_node = cmds.listConnections(shp, destination=True, t="shadingEngine")
                sg_nodes.extend(sg_node)

        sg_nodes = [sg for i, sg in enumerate(sg_nodes) if sg not in sg_nodes[:i]]
        return sg_nodes


    def export_sg_nodes(sg_nodes, file_path):
        """
        导出sg节点到ma文件
        """
        if len(sg_nodes) == 0:
            return False

        cmds.select(sg_nodes, r=True, ne=True)
        cmds.file(file_path, options="v=0;", typ="mayaAscii", pr=True, es=True)
        return True


    def export_all_sg_nodes(file_path):
        """
        导出所有sg节点
        """
        return export_sg_nodes(get_all_sg_nodes(), file_path)


    def export_sel_sg_nodes(file_path):
        """
        导出选择相关的sg节点
        """
        return export_sg_nodes(get_sel_sg_nodes(), file_path)


    def get_sg_members(sg_nodes=list()):
        """
        提取物体名字，判断不是transform类型，是shape的，就获取shape的父物体加到筛选列表里
        """
        data = dict()
        for sg in sg_nodes:
            members = cmds.sets(sg, q=True) or list()
            filter_members = list()
            for m in members:
                obj = m.split(".")
                if cmds.nodeType(obj[0]) != "transform":
                    obj[0] = cmds.listRelatives(obj[0], p=True)[0]
                filter_members.append(".".join(obj))

            data[sg] = filter_members

        return data


    def get_all_sg_members():
        """
        """
        return get_sg_members(get_all_sg_nodes())


    def get_sel_sg_members():
        """
        """
        return get_sg_members(get_sel_sg_nodes())


    def export_sg_members(data, file_path):
        """
        """
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        return True


    def export_all_sg_members(file_path):
        """
        """
        return export_sg_members(get_all_sg_members(), file_path)


    def export_sel_sg_members(file_path):
        """
        """
        return export_sg_members(get_sel_sg_members(), file_path)


    def reference_shader_file(file_path):
        """
        """
        # - 如果文件在场景的reference列表里，直接返回文件的namespace
        file_path = file_path.replace("\\", "/")
        ref_files = cmds.file(query=True, reference=True)
        if file_path in ref_files:
            return cmds.file(file_path, query=True, namespace=True)

        # - 如果文件没有reference过，就新re一份
        name_space = os.path.splitext(os.path.basename(file_path))[0]
        cmds.file(file_path, r=True, ns=name_space)
        return name_space


    def assign_data_to_all(data_path, sg_namespace=None, geo_namespace=None):
        """
        """
        data = dict()
        with open(data_path, "r") as f:
            data = json.load(f)

        for sg, geos in data.items():
            # - 先过滤sg节点场景里存在不存在
            if sg_namespace:
                sg = "{0}:{1}".format(sg_namespace, sg)
            if not cmds.objExists(sg):
                continue

            # - 过滤sg对应的物体是否都存在
            filter_items = list()
            for g in geos:
                g = "{0}:{1}".format(geo_namespace, g)
                if cmds.objExists(g.split(".")[0]):
                    filter_items.append(g)

            # - 连接sg节点与物体
            try:
                cmds.sets(filter_items, e=True, forceElement=sg)
            except:
                pass

    # export_sel_sg_nodes("D:/andy/lanzu.ma")
    # export_sel_sg_members("D:/andy/lanzu.json")

    assign_data_to_all("D:/andy/lanzu.json", "lanzu")