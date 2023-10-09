import time, os, json, hashlib
from LWApi import LWApi
from shutil import rmtree

def main():
    """Main function, it constites of a Menu where you can select
    an action to perform:
     - Get All AIs"""
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
    api.connect(principal["username"], principal["password"])

    menu = {}
    menu['1']="Get your AIs."
    menu['2']="Launch fight"
    menu['3']="Get Register"
    menu['4']="Get Farmer's Throphies"
    menu['5']="Push your AIs on secondary(ies) account(s)."
    menu['6']="Exit"
    while True:
        options=sorted(menu.keys())

        for entry in options:
            print(entry, menu[entry])

        selection=input("Please Select:")
        if selection =='1':
            get_all_ais(api, principal)
        elif selection == '2':
            print("delete")
        elif selection == '3':
            get_register(api,config)
        elif selection == '4':
            get_farmer_trophies(api, config["AIs_folder"])
            break
        elif selection == '5':
            push_all_ais(api, secondaries, config["AIs_folder"])
            break
        elif selection == '6':
            break
        else:
            print("Unknown Option Selected!")

def get_all_ais(api, root_folder):
    """Get all AIs from LeekWars, and save them in a directory location
    The folder hiearchie will be respected"""
    print("\nget_all_ais()\n")
    all_ais = api.get_ais()

    print("Delete previous files & folder under " + root_folder)
    if(os.path.exists(root_folder)):
        rmtree(root_folder)

    os.mkdir(root_folder)

    all_folders = { 0 : "./" }
    for folder in  all_ais["folders"]:
        all_folders[folder["id"]] = folder["name"]
        path = os.path.join(root_folder,folder["name"])
        if(not(os.path.exists(path))) :
            os.mkdir(path)

    for ai in  all_ais["ais"]:
        name = ai["name"]
        folder = os.path.join(root_folder,all_folders[ai["folder"]])
        code = api.get_ai(str(ai["id"]))["ai"]["code"]
        with open(os.path.join(folder,name+".leek"), "w") as outfile:
            outfile.write(code)
        time.sleep(0.2)

def push_all_ais(api, secondaries, root_folder):
    """Push all AIs from local directory onto LeekWars
    The folder hiearchie will be respected"""
    print("\npush_all_ais()\n")

    # List all local *.leek files and folders
    all_local_ais = get_local_ais(root_folder)

    # Per account, get all remote ias, to do the comparison
    for secondary in secondaries:
        api.connect(secondary["username"], secondary["password"])
        all_remote_ais = api.get_ais()




def Fight(api,config):
    print("\nFight()\n")


def get_register(api,config):
    print("\nRegister()\n")
    registers = api.get_registers("82210")
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
                    "folder": dirpath.replace(root_folder,'')
                })())
    return local_ais

# Here goes all the magic
main()
