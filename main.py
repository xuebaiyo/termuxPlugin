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
    
    def command_send(self, host: PluginHost, event: EventContext, command: str, **kwargs):
        if command == "t" or command == "termux":
            event.prevent_default()
            event.prevent_postorder()

            core_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
            sysmem_info = psutil.virtual_memory()
            cpu_info = psutil.cpu_times
            disk_info = psutil.disk_usage('/')
            cpu_ststs = psutil.cpu_stats()
            cpu_freq = psutil.cpu_freq()

            #获取用户输入的指令
            ossh = os.popen('ping 192.168.191.2').readlines()
            #print(ossh)
            
            res = f"""====执行结果====
CPU使用率: {psutil.cpu_percent(interval=1):.2f}%
执行结果: 
{ossh}
============"""

            event.add_return(
                "reply",
                [res.strip()]
            )
            
    @on(PersonCommandSent)
  def person_normal_message_received(self, event: EventContext, **kwargs):
        msg = kwargs['text_message']
        ossh = re.search(r"!(.*)", string)  #截取!号后所有字符
            # 输出测试结果
            ossh = os.popen('ping 192.168.191.2').readlines()
            # 回复消息 "hello, <发送者id>!"
            event.add_return("reply", ["命令执行结束!,直接结果为: {ossh}{}!".format(kwargs['sender_id'])])

            # 阻止该事件默认行为（向接口获取回复）
            event.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
