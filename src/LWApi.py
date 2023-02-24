import requests
import Uri

class LWApi:
    """Class LWApi. It will handle the call against the LeekWars Api."""

    def __init__(self):
        """Constructor of LWApi. Init the session."""
        self.__root_url = Uri.root
        self.__token = ""
        self.__session = requests.Session()

    def connect(self,login,password):
        """Connect to LeekWars Api and retrieve the auth token."""
        connection_string = Uri.login
        login_response = self.__session.post(self.__root_url + connection_string, data={ "login": login, "password": password}).json()
        self.__token = login_response["token"]

    def get_ias(self):
        """List all the IAs you have on LeekWars."""
        return self.__session.get(self.__root_url + Uri.get_ais, data={ "token": self.__token}).json()

    def get_ia(self,ai_id):
        """Get the IA file and its content."""
        return self.__session.get(self.__root_url + Uri.get_ai + "/" + ai_id, data={ "token": self.__token}).json()

    def get_scheme(self):
        """Not sure of what it is."""
        return self.__session.get(self.__root_url + Uri.get_scheme, data={ "token": self.__token}).json()

    def get_services(self):
        """List all the available endpoints of the LeekWars Api."""
        return self.__session.get(self.__root_url + Uri.get_services, data={ "token": self.__token}).json()

    def get_functions(self):
        """Get all the built-in functions of LeekScript."""
        return self.__session.get(self.__root_url + Uri.get_functions, data={ "token": self.__token}).json()

    def get_fullmoon(self):
        """Get all the date where a fullmoon occurs, or has occured."""
        return self.__session.get(self.__root_url + Uri.get_fullmoon, data={ "token": self.__token}).json()

    def get_doc_functions(self, langue):
        """Get the full documention of built-in functions. Only 'fr' the currently supported as locale"""
        return self.__session.get(self.__root_url + Uri.get_doc_functions.replace("locale",langue), data={ "token": self.__token}).json()

    def get_registers(self, leek_id):
        """Get the registers of the given {leek}"""
        return self.__session.get(self.__root_url + Uri.get_registers.replace("leek_id", leek_id), data={ "token": self.__token}).json()

    def delete_register(self, leek_id, register_key):
        """Delete the register {key} of the given {leek}"""
        return self.__session.post(self.__root_url + Uri.delete_register.replace("leek_id", leek_id).replace("key", register_key), data={ "token": self.__token}).json()

    def set_register(self, leek_id, register_key, register_value):
        """Set the register {key} with {value} of the given {leek}"""
        return self.__session.post(self.__root_url + Uri.set_register.replace("leek_id", leek_id).replace("key", register_key).replace("value",register_value), data={ "token": self.__token}).json()

    def get_farmer_trophies(self, farmer_id):
        """Get trophies list of the given {farmer}"""
        return self.__session.get(self.__root_url + Uri.get_farmer_trophies.replace("farmer_id", farmer_id,).replace("lang","fr"), data={ "token": self.__token, "farmer_id": farmer_id, "lang":"fr"}).json()

    def get_farmer_history(self, leek_id):
        """Get the registers of the given {leek}"""
        return self.__session.get(self.__root_url + Uri.get_registers.replace("leek_id", leek_id), data={ "token": self.__token}).json()