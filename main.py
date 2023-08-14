from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

import os
import psutil
import re

# 注册插件
@register(name="termux", description="执行终端指令", version="0.2", author="xuebaiyo")
class SysStatPlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass

    @on(GroupCommandSent)
    @on(PersonCommandSent)
  def person_normal_message_received(self, event: EventContext, **kwargs):
        msg = kwargs['text_message']
       result = re.search(r"!ossh(.*)", msg)  #截取!ossh后所有字符
      if result:
            matched_text = result.group(1)            # 获取匹配到的结果
            ossh = os.popen(matched_text).readlines()  #执行指令
            event.add_return("reply", ["命令执行结束!,直接结果为: {ossh}{}!".format(kwargs['sender_id'])])

            # 阻止该事件默认行为（向接口获取回复）
            event.prevent_default()

else:
   # print("未找到匹配的内容")
            # 回复消息 "hello, <发送者id>!"
            event.add_return("reply", ["请在!t 后面输入指令!,{}!".format(kwargs['sender_id'])])

            # 阻止该事件默认行为（向接口获取回复）
            event.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
