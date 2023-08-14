import logging
from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

@register(name="ossh", description="通过qbot执行linux命令", version="0.1", author="xuebaiyo")
class HelloPlugin(Plugin):
    def __init__(self, plugin_host: PluginHost):
        pass

    @on(PersonNormalMessageReceived)
    def person_normal_message_received(self, event: EventContext, **kwargs):
        msg = kwargs['text_message']
        if "ossh" in msg:  # 如果消息中包含"ossh"字段

            # 输出调试信息
            logging.debug("ossh command received from {}".format(kwargs['sender_id']))

            # 截取"ossh"后面的所有字符
            command = msg.split("ossh", 1)[1].strip()

            # 执行相应的操作，例如调用Linux命令
            # ...

            # 回复消息
            event.add_return("reply", ["执行了ossh命令"])

            # 阻止该事件默认行为（向接口获取回复）
            event.prevent_default()

    def __del__(self):
        pass
