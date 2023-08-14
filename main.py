from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

import os
import psutil


# 注册插件
@register(name="termux", description="执行终端指令", version="0.1", author="xuebaiyo")
class SysStatPlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass

    @on(GroupCommandSent)
    @on(PersonCommandSent)
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

    # 插件卸载时触发
    def __del__(self):
        pass
