=============================
Python内置模块：re
=============================

正则表达式模块re

.. code-block:: python

    import re
    from pprint import pprint

    files = ["tank_1_color_v0.rat",
             "tank_2_color_v5.rat",
             "tank_1_color_v3.rat",
             "tank_3_color_v1.rat",
             "tank_4_color_v2.rat",
             "tank_4_color_v4.rat",
             "tank_5_color_v1.rat",
             "tank_6_color_v6.rat"]

    pat_num = re.compile("\D+_(\d+)_")
    pat_ver = re.compile("(\d+)\D+$")

    def sorter_num(elem):
        res = re.search(pat_num, elem)
        return res.groups()[0]

    def sorter_ver(elem):
        res = re.search(pat_ver, elem)
        return res.groups()[0]

    # pprint(sorted(files, key=sorter_num))
    pprint(sorted(files, key=sorter_ver))
