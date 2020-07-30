=============================
Deadline渲染农场提交农场接口
=============================

使用Deadline Python API提交任务需要开启deadlinewebservice.exe服务。

.. code-block:: python

    >>> import sys
    >>>
    >>>
    >>> path = r"Y:\Program\DeadlineRepository10\api\python"
    >>>
    >>> path in sys.path or sys.path.insert(0, path)
    >>> import Deadline.DeadlineConnect as Connect
    >>> con = Connect.DeadlineCon("192.168.0.111", 8082)
    >>> con
    <Deadline.DeadlineConnect.DeadlineCon instance at 0x00E90B48>
    >>> type(con)
    <type 'instance'>
    >>>
    >>>
    >>>
    >>> dir(con)
    ['AuthenticationModeEnabled', 'Balancer', 'EnableAuthentication', 'Groups', 'JobReports', 'Jobs', 'LimitGroups', 'MappedPaths', 'MaximumPriority', 'Plugins', 'Pools', 'Pulse', 'Repository', 'SetAuthenticationCredentials', 'Slaves', 'SlavesRenderingJob', 'TaskReports', 'Tasks', 'Users', '__doc__', '__init__', '__module__', 'connectionProperties']
    >>>
    >>>
    >>> con.Groups
    <Deadline.Groups.Groups instance at 0x00E90DA0>
    >>> dir(con.Groups)
    ['AddGroup', 'AddGroups', 'DeleteGroup', 'DeleteGroups', 'GetGroupNames', 'PurgeGroups', '__doc__', '__init__', '__module__', 'connectionProperties']
    >>> con.Groups.GetGroupNames()
    [u'none', u'nuke', u'arnold', u'cache', u'gpu', u'maya2016', u'largem', u'core48', u'pdg', u'maya2017', u'rs3', u'maya2018']
    >>>
    >>> job = con.Jobs.GetJob("5f16b24ab3a4a507c0359b71")
    >>> type(job)
    <type 'dict'>
    >>> from pprint import pprint
    >>> pprint(job)
    >>> job["Props"]["Pri"] = 97
    >>> pprint(job)
    >>> con.Jobs.SaveJob(job)
    'Success'
    >>>
