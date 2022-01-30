import sys
import os
from flowlauncher import FlowLauncher
import re
from plugin.helper import Actions

plugindir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(plugindir)
sys.path.append(os.path.join(plugindir, "lib"))
sys.path.append(os.path.join(plugindir, "plugin"))


class QuickerActionSearch(FlowLauncher):
    def query(self, param: str = ''):
        jsonlist = []
        searchObj = re.search(r'[一-龥]', param)
        act = Actions()
        act_dict = act.actions(searchObj)
        for item in act_dict.keys():
            if item.find(param) != -1:
                act_list = act_dict[item]
                jsonlist.append({"Title": act_list[1], "SubTitle": act_list[2], "IcoPath": "Images/app.png",
                                 "JsonRPCAction": {"method": "exec_action", "parameters": [act_list[0]]},
                                 "scores": 0})

        return jsonlist

    def context_menu(self, data):
        return [
            {
                "Title": "Hello World Python's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                }
            }
        ]

    def exec_action(self, paras):
        os.system("start quicker:runaction:{0}".format(paras))


if __name__ == "__main__":
    QuickerActionSearch()
