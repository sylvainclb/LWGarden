import time
from LWApi import LWApi
import os
import json

with open("config.json", "r") as configfile:
    config = json.load(configfile)


api = LWApi()
api.connect(config["username"], config["password"])

def GetAllIAs():
    print("GetAllIAs()")
    allAIs = api.getIAs()

    allFolders = { 0 : "./" } 
    for folder in  allAIs["folders"]:
        allFolders[folder["id"]] = folder["name"]
        path = os.path.join(config["AIs_folder"],folder["name"])
        if(not(os.path.exists(path))) :
            os.mkdir(path)

    for ai in  allAIs["ais"]:
        name = ai["name"]
        folder = os.path.join(config["AIs_folder"],allFolders[ai["folder"]])
        code = api.getIA(str(ai["id"]))["ai"]["code"]
        with open(os.path.join(folder,name+".leek"), "w") as outfile:
            outfile.write(code)
        time.sleep(0.2)

GetAllIAs()
# print(api.getScheme())
# print(api.getServices())
#functions = api.getFunctions()
#print(functions["functions"][0])
doc = api.getDocFunctions("fr")
print(doc["getTimestamp"])
# with open("doc.json", "w") as docfile:
#     json.dump(doc,docfile)
# print(api.getFullMoon())