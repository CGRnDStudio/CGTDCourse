=========================================
Rocket.Chat免费聊天工具部署
=========================================

.. code-block:: python

    from rocketchat_API.rocketchat import RocketChat

    rocket = RocketChat("Robot", "<password>", server_url="http://192.168.0.244:3000")
    rocket.chat_post_message("@Andy test!", channel="general")
