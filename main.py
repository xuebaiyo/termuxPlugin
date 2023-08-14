import re
import subprocess
from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

@register(name="ossh", description="通过qbot执行linux命令", version="0.1", author="xuebaiyo")
class HelloPlugin(Plugin):
    def __init__(self, plugin_host: PluginHost):
        pass

    @on(PersonNormalMessageReceived)
    def person_normal_message_received(self, event: EventContext, **kwargs):
        msg = kwargs['text_message']
        if "ossh" in msg:  # 判断消息是否包含"ossh"字段
            # 使用正则表达式截取"ossh"后面的所有字符
            result = re.search(r"ossh(.*)", msg)
            if result:
                command = result.group(1).strip()  # 获取截取到的命令，并去除首尾空格

                try:
                    # 执行Linux命令
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                    # 回复执行结果
                    event.add_return("reply", [output])
                except subprocess.CalledProcessError as e:
                    error_output = e.output if e.output else str(e)
                    # 回复错误信息
                    event.add_return("reply", ["命令执行出错：{}".format(error_output)])
            else:
                event.add_return("reply", ["未找到要执行的命令"])
            
            event.prevent_default()

    def __del__(self):
        pass
