import csv
import os
import json
actionNameList = []
actionDict = {}
with open('../quickeractions.csv') as f:
    f_csv = csv.reader(f)
    for index, row in enumerate(f_csv):
        print(row)
        if index == 0 or index == 1:
            continue
        actionDict[row[1]] = row
        actionNameList.append(row[1])

# print(actionNameList)
# print(actionDict)
# os.system("start quicker:runaction:283c555a-8804-4398-9610-83e3ffb9dcbd")
# a=json.loads('''{"title":"Hello World, this is where title goes. {}","subTitle":"This is where your subtitle goes, press enter to open Flow's url","icoPath":"Images/app.png","jsonRPCAction":{"method":"open_url","parameters":["https://github.com/Flow-Launcher/Flow.Launcher"]},"score":0}''')
# print(a)
# print(a['jsonRPCAction'])
# print(type(a['jsonRPCAction']))
# print(type(a))
# b=json.dumps(a)
# print(b)