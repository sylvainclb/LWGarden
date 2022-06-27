import json
from multiprocessing.dummy import connection
import requests
import Uri
import collections

class LWApi:
    
    def __init__(self):
        self.__rootUrl = Uri.Root
        self.__token = ""
        self.session = requests.Session()

    def connect(self,login,password):
        connectionString = Uri.Login.replace("Login",login).replace("Password",password)
        self.__token = self.session.get(self.__rootUrl + connectionString).json()["token"]

    def getIAs(self):
        return self.session.get(self.__rootUrl + Uri.GetAIs, data={ " token": self.__token}).json()

    def getIA(self,ai_id):
        return self.session.get(self.__rootUrl + Uri.GetAI +"/"+ai_id, data={ " token": self.__token}).json()

    def getScheme(self):
        return self.session.get(self.__rootUrl + Uri.GetScheme, data={ " token": self.__token}).json()
    
    def getServices(self):
        return self.session.get(self.__rootUrl + Uri.GetServices, data={ " token": self.__token}).json()

    def getFunctions(self):
        return self.session.get(self.__rootUrl + Uri.GetFunctions, data={ " token": self.__token}).json()
    
    def getFullMoon(self):
        return self.session.get(self.__rootUrl + Uri.GetFullMoon, data={ " token": self.__token}).json()