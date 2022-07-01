import requests
import Uri

class LWApi:
"""Calss LWApi. It will handle the call against the LeekWars Api."""

    def __init__(self):
        """Constructor of LWApi. Init the session."""
        self.__rootUrl = Uri.Root
        self.__token = ""
        self.__session = requests.Session()

    def connect(self,login,password):
        """Connect to LeekWars Api and retrieve the auth token."""
        connectionString = Uri.Login.replace("Login",login).replace("Password",password)
        self.__token = self.__session.get(self.__rootUrl + connectionString).json()["token"]

    def getIAs(self):
        """List all the IAs you have on LeekWars."""
        return self.__session.get(self.__rootUrl + Uri.GetAIs, data={ " token": self.__token}).json()

    def getIA(self,ai_id):
        """Get the IA file and its content."""
        return self.__session.get(self.__rootUrl + Uri.GetAI +"/"+ai_id, data={ " token": self.__token}).json()

    def getScheme(self):
        """Not sure of what it is."""
        return self.__session.get(self.__rootUrl + Uri.GetScheme, data={ " token": self.__token}).json()

    def getServices(self):
        """List all the available endpoints of the LeekWars Api."""
        return self.__session.get(self.__rootUrl + Uri.GetServices, data={ " token": self.__token}).json()

    def getFunctions(self):
        """Get all the built-in functions of LeekScript."""
        return self.__session.get(self.__rootUrl + Uri.GetFunctions, data={ " token": self.__token}).json()

    def getFullMoon(self):
        """Get all the date where a full moon occurs, or has occured."""
        return self.__session.get(self.__rootUrl + Uri.GetFullMoon, data={ " token": self.__token}).json()

    def getDocFunctions(self, langue):
        """Get the full documention of built-in functions. Only 'fr' the currently supported as locale"""
        return self.__session.get(self.__rootUrl + Uri.GetDocFunctions.replace("locale",langue), data={ " token": self.__token}).json()
