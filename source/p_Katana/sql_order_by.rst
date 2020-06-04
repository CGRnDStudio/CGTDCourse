=========================================
SQL查询按数字排序
=========================================

这里要特别注意如果字段是字符串类型的数字，需要转换int类型再做排序，不然会出问题。

.. code-block:: python

    SELECT version_number FROM publishedfile WHERE task__id = 11086 and _active = 't' ORDER BY CAST(version_number AS int)
