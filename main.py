import sys
import os
from flowlauncher import FlowLauncher
import csv

plugindir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(plugindir)
sys.path.append(os.path.join(plugindir, "lib"))
sys.path.append(os.path.join(plugindir, "plugin"))

actiondict = {}
jsonlist = []
with open('quickeractions.csv') as f:
    f_csv = csv.reader(f)
    for index, row in enumerate(f_csv):
        if index == 0 or index == 1:
            continue
        actiondict[row[1]] = row
for item in actiondict.keys():
    actionlist = actiondict[item]
    tempdict = {"Title": item, "SubTitle": actionlist[2], "IcoPath": "Images/app.png",
                "JsonRPCAction": {"method": "exec_action", "parameters": [actionlist[0]]}, "scores": 0}

    jsonlist.append(tempdict)
class QuickerActionSearch(FlowLauncher):
    # def __init__(self):
    #     self.actiondict = {}
    #     self.jsonlist = []
    #     with open('quickeractions.csv') as f:
    #         f_csv = csv.reader(f)
    #         for index, row in enumerate(f_csv):
    #             if index == 0 or index == 1:
    #                 continue
    #             self.actiondict[row[1]] = row
    #     for item in self.actiondict.keys():
    #         actionlist = self.actiondict[item]
    #         tempdict = {"Title": item, "SubTitle": actionlist[2], "IcoPath": "Images/app.png",
    #                     "JsonRPCAction": {"method": "exec_action", "parameters": actionlist[0]}, "scores": 0}
    #
    #         self.jsonlist.append(tempdict)

    def query(self, param: str = ''):
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


    def exec_action(self, action_id):
        os.system("start quicker:runaction:{0}".format(action_id))


if __name__ == "__main__":
    QuickerActionSearch()
