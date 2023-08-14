from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
import subprocess

# 注册插件
@register(name="SysStat", description="查看系统状态", version="0.1", author="RockChinQ")
class SysStatPlugin(Plugin):

    def __init__(self, plugin_host: PluginHost):
        pass

    @on(GroupCommandSent)
    @on(PersonCommandSent)
    def command_send(self, host: PluginHost, event: EventContext, command: str, **kwargs):
        if command.startswith("ossh"):
            event.prevent_default()
            event.prevent_postorder()

            linux_command = command[5:]  # 去除"ossh"前缀，获取Linux命令部分
            try:
                result = subprocess.check_output(linux_command, shell=True, stderr=subprocess.STDOUT)
                res = result.decode("utf-8")
            except subprocess.CalledProcessError as e:
                res = f"命令执行出错：{e.output.decode('utf-8')}"

            event.add_return(
                "reply",
                [res.strip()]
            )

    def __del__(self):
        pass
