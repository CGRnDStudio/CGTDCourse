=============================
Python内置模块：json
=============================

json (JavaScript Object Notation) 是一种轻量级的数据交换格式。

.. code-block:: python

    >>> import json
    >>> json.__file__
    'C:\\Python27\\lib\\json\\__init__.pyc'
    >>> type(json)
    <type 'module'>
    >>> dir(json)
    ['JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__version__', '_default_decoder', '_default_encoder', 'decoder', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']
    >>>

- json.dump 字典转文件
- json.dumps 字典转字符串
- json.load 文件转字典
- json.loads 字符串转字典

.. code-block:: python

    import json

    data = {
        "name": "Andy",
        "age": 29,
        "weight": 55.5
    }

    jsonStr = json.dumps(data)

    jsonData = json.loads(jsonStr)

    # Writing JSON data
    with open("data.json", "w") as f:
        json.dump(data, f)

    # indent用法
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    with open("data.json", "r") as f:
        data = json.load(f)
