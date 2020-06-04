=========================================
SQL查询按字段打组
=========================================

GROUP BY是个很有意思的操作。

.. code-block:: python

    SELECT new.code, path_cache, version_number, task__id, published_file_type__id, new.created_by__id, new.created_at, humanuser.name, publishedfiletype.code AS file_type, content FROM (SELECT code, path_cache, max.version_number, max.task__id, published_file_type__id, created_by__id, created_at, name FROM (SELECT task__id, MAX(version_number) AS version_number FROM publishedfile WHERE project__id=%d AND entity__id=%d AND _active='t' GROUP BY task__id, published_file_type__id) max JOIN publishedfile ON max.task__id=publishedfile.task__id AND max.version_number=publishedfile.version_number AND _active='t') new, publishedfiletype, humanuser, task WHERE new.published_file_type__id=publishedfiletype.id AND new.created_by__id=humanuser.id AND new.task__id=task.id
