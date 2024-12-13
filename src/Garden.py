import time, os, json, hashlib
from LWApi import LWApi
from shutil import rmtree
import json


def main():
    """Main function, it constites of a Menu where you can select
    an action to perform:
    """
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██████▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁████▓▓▓▓▓▓████▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁████▁▁██▓▓▓▓▓▓▓▓▓▓██▁▁████▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁██▓▓▓▓████▓▓▓▓▓▓▓▓▓▓████▓▓▓▓██▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▁▁▁▁")
    print("▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓██▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓██▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁██▁▁██▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁██▁▁██▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▒▒▒▒▁▁▒▒▒▒██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██████▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")

    print("\nWelcome to the Leek Garden, a tool to empower your leeks on LeekWars!")

    print("\nTry to login on the LeekWars Api, please ensure that a config.json is present, with your username and password")
    with open("./src/config.json", "r") as configfile:
        config = json.load(configfile)
    api = LWApi()
    accounts = config["accounts"]
    principal= next(p for p in accounts if p["primary"] == 'true')
    secondaries = list(p for p in accounts if p["primary"] == 'false')
    response_connect = api.connect(principal["username"], principal["password"])
    if response_connect:
        farmer = api.get_farmer()
        print("\nYou are connected as {farmer_name}".format(farmer_name=farmer["name"]))
    else:
        print("\nCannot connect to LW account with ID {user_name}\n".format(user_name=principal["username"]))
        exit()

    menu = {}
    menu['1']="Get your AIs."
    menu['2']="Push your AIs on secondary(ies) account(s)."
    menu['3']="Sync IAs from primary account to your secondary(ies) account(s)."
    menu['4']="Launch fight"
    menu['5']="Get Register"
    menu['6']="Get Farmer's Throphies"
    menu['7']="Buy Fights"
    menu['8']="Register to tournament"
    menu['9']="Exit"
    while True:
        options=sorted(menu.keys())

        print("\n")

        for entry in options:
            print(entry, menu[entry])

        selection=input("Please Select:")
        if selection =='1':
            get_all_ais(api, config["AIs_folder"])
        elif selection == '2':
            push_all_ais(api, secondaries, config["AIs_folder"])
            # reconnect to the main
            api.connect(principal["username"], principal["password"])
        elif selection == '3':
            get_all_ais(api, config["AIs_folder"])
            push_all_ais(api, secondaries, config["AIs_folder"])
            # reconnect to the main
            api.connect(principal["username"], principal["password"])
        elif selection == '4':
            print('TO TO')
        elif selection == '5':
            get_register(api,config)
        elif selection == '6':
            get_farmer_trophies(api, config["AIs_folder"])
        elif selection == '7':
            buy_fights(api, config["accounts"])
        elif selection == '8':
            register_tournaments(api, config["accounts"])
        elif selection == '9':
            break
        else:
            print(" Unknown Option Selected!")

def buildFolder(folders, all_folders, folder, currentPath):
    if len(folders) == 0:
        return
    path = os.path.join(currentPath,folder["name"])

    if(not(os.path.exists(path))) :
        os.mkdir(path)
    all_folders[folder["id"]] = path

    folders = [f for f in folders if f["id"] != folder["id"]]

    for f in folders:
        if f["folder"] == folder["id"]:
            buildFolder(folders, all_folders, f, path)

def get_all_ais(api, root_folder : str):
    """Get all AIs from LeekWars, and save them in a directory location
    The folder hiearchie will be respected"""
    print("\nget_all_ais()\n")
    all_ais = api.get_ais()

    print("Delete previous files & folder under " + root_folder)
    if(os.path.exists(root_folder)):
        rmtree(root_folder)

    os.mkdir(root_folder)

    all_folders = { 0 : root_folder }
    folders = all_ais["folders"][:]
    for folder in all_ais["folders"]:
        if folder["folder"] == 0:
            buildFolder(folders, all_folders, folder, root_folder)

    for ai in  all_ais["ais"]:
        name = ai["name"]
        folder = all_folders[ai["folder"]]
        code = api.get_ai(str(ai["id"]))["ai"]["code"]
        with open(os.path.join(folder,name+".leek"), "w") as outfile:
            outfile.write(code)
        time.sleep(0.2) # we need to wait a little, to not be throttle

def push_all_ais(api, secondaries, root_folder):
    """Push all AIs from local directory onto LeekWars
    The folder hiearchie will be respected"""
    print("\npush_all_ais()\n")

    # List all local *.leek files and folders
    all_local_ais = get_local_ais(root_folder)

    all_local_folders = [x for x in all_local_ais if x.type == "folder"]
    all_local_folders.sort(key=lambda x: x.folder, reverse=False)
    all_local_files = [x for x in all_local_ais if x.type == "file"]

    # Per account, get all remote ias, to do the comparison
    for secondary in secondaries:
        api.connect(secondary["username"], secondary["password"])["farmer"]
        farmer2 = api.get_farmer()
        print("\nPush to the account {farmer_name}\n".format(farmer_name=farmer2["login"]))
        all_remote_ais = api.get_ais()

        # Loop on local folder and create in remote if not exists
        for local_folder in all_local_folders:
            if not any(x["name"] == local_folder.name for x in all_remote_ais["folders"]):
                print("\tCreate folder: " + local_folder.name)
                parent_folder_id = 0
                if local_folder.folder != '':
                    parent = [x for x in all_remote_ais["folders"] if x["name"] == local_folder.folder]
                    parent_folder_id = parent[0]["id"]
                result = api.new_folder(local_folder.name,parent_folder_id)
                if result.ok:
                    jsonResult = result.json()
                    new_folder = {
                    "id": jsonResult["id"],
                    "name": local_folder.name,
                    "folder": parent_folder_id
                    }
                    all_remote_ais["folders"].append(new_folder)



        # Loop on local ais and create in remote if not exists
        # if exists, compare hash to see if we need to update the remote file
        for local_file in all_local_files:
            if not any(x["name"] == local_file.name for x in all_remote_ais["ais"]):
                print("\tCreate ai: " + local_file.name, end="")
                parent_folder_id = 0
                if local_file.folder != '':
                    parent = [x for x in all_remote_ais["folders"] if x["name"] == local_file.folder]
                    parent_folder_id = parent[0]["id"]
                result = api.new_ai(local_file.name,parent_folder_id)
                if result.ok:
                    jsonResult = result.json()
                    new_ai = {
                        "id":jsonResult["ai"]["id"],
                        "name": local_file.name,
                        "folder": parent_folder_id,
                        "code": local_file.content,
                        "level": jsonResult["ai"]["level"]
                    }
                    resultSave = api.save_ai(new_ai["id"],new_ai["code"])
                    if resultSave.ok:
                        all_remote_ais["ais"].append(new_ai)
                        print(" -> Done!")
                    else:
                        print(" -> K.O. ... " + resultSave.content)
                    time.sleep(0.2) # we need to wait a little, to not be throttle
                else:
                    print(" -> K.O. ... " + result.content)
                time.sleep(0.2) # we need to wait a little, to not be throttle
            else:
                remote_file = [x for x in all_remote_ais["ais"] if x["name"] == local_file.name]
                remote_code = api.get_ai(str(remote_file[0]["id"]))["ai"]["code"]
                remote_hash = hashlib.sha512(remote_code.encode('utf-8')).hexdigest()
                if remote_hash != local_file.hash:
                    print("\tUpdate ai " + local_file.name, end="")
                    resultSave = api.save_ai(remote_file[0]["id"],local_file.content)
                    if resultSave.ok:
                        print(" -> Done!")
                    else:
                        print(" -> K.O. ... " + resultSave.content)
                time.sleep(0.2) # we need to wait a little, to not be throttle


        for ai in  all_remote_ais["ais"]:
            if not any( x.name == ai["name"] for x in all_local_files):
                print("\tDelete ai: " + ai["name"], end="")
                resultDelete = api.delete_ai(ai["id"])
                if resultDelete.ok:
                    print(" -> Done!")
                else:
                    print(" -> K.O. ... " + resultDelete.content)
                time.sleep(0.2) # we need to wait a little, to not be throttle

        for folder in all_remote_ais["folders"]:
            if not any( x.name == folder["name"] for x in all_local_folders):
                print("\tDelete folder: " + folder["name"], end="")
                resultDelete = api.delete_folder(folder["id"])
                if resultDelete.ok:
                    print(" -> Done!")
                else:
                    print(" -> K.O. ... " + resultDelete.content)
                time.sleep(0.2) # we need to wait a little, to not be throttle


def Fight(api,config):
    print("\nFight()\n")


def get_register(api,config):
    print("\nRegister()\n")
    registers = api.get_registers(82210)
    menu ={}
    i=0
    for register in registers["registers"]:
        menu[str(i)]= register["key"]
        i+=1

    while True:
        options=sorted(menu.keys())
        for entry in options:
            print(entry, menu[entry])
        selection=input("Please Select: (input any other key to exit)")
        if options.__contains__(selection):
            selected_register = next(filter(lambda x: x["key"] == menu[selection] , registers["registers"]))
            last = sorted(json.loads(selected_register["value"]).values(), reverse=True)
            print(last)
            somme = sum(last)
            total = len(last)
            print(somme/total)
            print(last[0])
        else:
            break
        print("\n")

def get_farmer_trophies(api,config):
    selection=input("Please enter farmer id: ")
    trophies= api.get_farmer_trophies(selection)
    pyro = next(filter(lambda x: x["code"] == "explorator" , trophies["trophies"]))
    print(pyro)

def get_local_ais(root_folder, local_ais = [], ext = "*.leek"):
    """recursive function to get all AIs"""
    # walk() is working recursively
    for (dirpath, dirnames, filenames) in os.walk(root_folder):
        for filename in filenames:
            with open(os.path.join(dirpath,filename), 'r') as file:
                filecontent = file.read()
                local_ais.append(type('',(object,),{
                    "name": filename.replace('.leek',''),
                    "content" : filecontent,
                    "hash": hashlib.sha512(filecontent.encode('utf-8')).hexdigest(),
                    "folder": os.path.basename(dirpath.replace(root_folder,'')),
                    "type": "file"
                })())
        for dirname in dirnames:
            local_ais.append(type('',(object,),{
                    "name": dirname ,
                    "content" : "",
                    "hash": "",
                    "folder": os.path.basename(dirpath.replace(root_folder,'')),
                    "type": "folder"
                })())
    return local_ais

def buy_fights(api, accounts):
    """Buy 50 fights with habs for all accounts"""
    connected_username = api.get_connected_username()
    for account in accounts:
        if(connected_username != account["username"]):
            api.connect(account["username"], account["password"])
        farmer = api.get_farmer()
        print("\nBuy 50 fights for the account {farmer_name}\n".format(farmer_name=farmer["name"]))
        buy_response = api.buy_fights()
        if "fights" in buy_response:
            print("Buying 50 fights: OK. ")
        else:
            print(buy_response['error'] + " when trying to buy 50 fights")

def register_tournaments(api, accounts):
    """Register for tournaments, for all accounts if required"""
    connected_username = api.get_connected_username()
    for account in accounts:
        if (any(account["Tournaments"][tournament] == True for tournament in account["Tournaments"])):
            if (connected_username != account["username"]):
                api.connect(account["username"], account["password"])
            farmer = api.get_farmer()
            print("\nRegister to tournaments for the account {farmer_name} : ".format(farmer_name=farmer["name"]))
            if(account["Tournaments"]["Farmer"]):
                """register for farmer"""
                print("\t > Farmer:", end=" ")
                register_response = api.register_tournament_farmer()
                if (register_response and len(register_response) > 0):
                    print(register_response["error"])
                else:
                    print("register OK")

            for leek_id in farmer["leeks"]:
                leek = api.get_leek(int(leek_id))
                if(account["Tournaments"]["Solo"]):
                    """register all solo"""
                    print("\t > Solo {leek_name}:".format(leek_name=leek["name"]), end=" ")
                    if leek["tournament"]["registered"]:
                        print("register OK")
                    else:
                        register_response = api.register_tournament_leek(int(leek_id))
                        if (register_response and len(register_response) > 0):
                            print(register_response["error"])
                        else:
                            print("register OK")

                if(account["Tournaments"]["BattleRoyal"]):
                    """register all auto BR"""
                    print("\t > BR {leek_name}:".format(leek_name=leek["name"]), end=" ")
                    if leek["auto_br"]:
                        print("register OK")
                    else:
                        register_response = api.register_tournament_battle_royal(int(leek_id))
                        if (register_response and len(register_response) > 0):
                            print(register_response["error"])
                        else:
                            print("register OK")

# Here goes all the magic
main()
