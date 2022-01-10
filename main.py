import json
import sys
import os
from flowlauncher import FlowLauncher
import csv

plugindir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(plugindir)
sys.path.append(os.path.join(plugindir, "lib"))
sys.path.append(os.path.join(plugindir, "plugin"))


class QuickerActionSearch(FlowLauncher):
    def __init__(self):
        self.actionnamelist = []
        self.actiondict = {}
        self.jsonlist = []
        with open('quickeractions.csv') as f:
            f_csv = csv.reader(f)
            for index, row in enumerate(f_csv):
                if index == 0 or index == 1:
                    continue
                self.actiondict[row[1]] = row
                self.actionnamelist.append(row[1])
        for item in self.actionnamelist:
            actionlist = self.actiondict[item]
            tempdict = {'title': item, 'subTitle': actionlist[2], 'icoPath': 'Images/app.png',
                        'jsonRPCAction': {'method': 'exec_action', 'parameters': actionlist[0]}, 'score': 0}

            self.jsonlist.append(tempdict)

    def query(self, query):
        return [
            {
                "title": "Hello World, this is where title goes. {}".format(('Your query is: ' + query , query)[query == '']),
                "subTitle": "This is where your subtitle goes, press enter to open Flow's url",
                "icoPath": "Images/app.png",
                "jsonRPCAction": {
                    "method": "exec_action",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher"]
                },
                "score": 0
            }
        ]


    # def context_menu(self, data):
    #     return [
    #         {
    #             "title": "Hello World Python's Context menu",
    #             "subTitle": "Press enter to open Flow the plugin's repo in GitHub",
    #             "icoPath": "Images/app.png",  # related path to the image
    #             "jsonRPCAction": {
    #                 "method": "open_url",
    #                 "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
    #             },
    #             "score": 0
    #         }
    #     ]
    def exec_action(self, action_id):
        os.system("start quicker:runaction:{0}".format(action_id))


if __name__ == "__main__":
    u=QuickerActionSearch()
    print(u.jsonlist)
