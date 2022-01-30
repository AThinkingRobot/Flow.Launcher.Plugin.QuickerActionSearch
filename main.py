import sys
import os
from flowlauncher import FlowLauncher
import re
from plugin.helper import Actions
import webbrowser
import pyperclip

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
                jsonlist.append({"Title": act_list[1], "SubTitle": act_list[2], "IcoPath": act_list[3],
                                 "JsonRPCAction": {"method": "exec_action", "parameters": [act_list[0]], "scores": 0},
                                 "ContextData": [act_list[13],act_list[0]]}
                                )

        return jsonlist

    def context_menu(self, data):
        return [
            {
                "Title": "打开动作网页",
                "SubTitle": data[0],
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [data[0]]
                }
            },
            {
                "Title": "复制动作id",
                "SubTitle": data[1],
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [data[1]]
                }
            }
        ]

    def exec_action(self, paras):
        os.system('"C:\Program Files\Quicker\QuickerStarter.exe" runaction:{0}'.format(paras))
        # os.system("start /B quicker:runaction:{0}".format(paras))

    def open_url(self, url):
        webbrowser.open(url)

    def copy_action_id(self,action_id):
        pyperclip.copy(action_id)



if __name__ == "__main__":
    QuickerActionSearch()
