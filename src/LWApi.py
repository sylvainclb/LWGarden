import requests
import Uri

class LWApi:
    """Class LWApi. It will handle the call against the LeekWars Api."""

    def __init__(self):
        """Constructor of LWApi. Init the session."""
        self.__root_url = Uri.root
        self.__token = ""
        self.__username = ""
        self.__session = requests.Session()

    def connect(self,login,password):
        """Connect to LeekWars Api and retrieve the auth token."""
        connection_string = Uri.login
        try:
            login_response = self.__session.post(self.__root_url + connection_string, data={ "login": login, "password": password}).json()
            self.__token = login_response["token"]
            self.__username = login
        except:
            return False
        else:
            return True

    def get_connected_username(self):
        return self.__username;

    def get_farmer_self(self):
        """Get you farmer object, based on the connected LeekWars account."""
        return self.__session.get(self.__root_url + Uri.get_self, data={ "token": self.__token}).json()

    # Section AI
    def get_ais(self):
        """List all the AIs you have on LeekWars."""
        return self.__session.get(self.__root_url + Uri.get_ais, data={ "token": self.__token}).json()

    def get_ai(self,ai_id):
        """Get the AI file and its content."""
        return self.__session.get(self.__root_url + Uri.get_ai + "/{ai_id}".format(ai_id=str(ai_id)), data={ "token": self.__token, "ai_id": str(ai_id) }).json()
    
    def new_ai(self, ai_name, folder_id = 0, ls_version = 4):
        """Create a new ai file in LW"""
        return self.__session.post(self.__root_url + Uri.new_ai, data={ "token": self.__token, "folder_id": str(folder_id), "name": ai_name, "version": str(ls_version)} )
 
    def save_ai(self, ai_id, ai_code):
        """Save an ai into LW"""
        return self.__session.post(self.__root_url + Uri.save_ai, data={ "token": self.__token, "ai_id": str(ai_id), "code": ai_code } )
    
    def rename_ai(self, ai_id, ai_name):
        """Rename an AI file"""
        return self.__session.post(self.__root_url + Uri.rename_ai , data={ "token": self.__token, "ai_id": ai_id, "ai_name": ai_name}).json()
    
    def new_folder(self, folder_name, parent_folder_id = 0):
        """Create a new folder in LW"""
        return self.__session.post(self.__root_url + Uri.new_folder_ai, data={ "token": self.__token, "folder_id": str(parent_folder_id), "name": folder_name} )

    def delete_ai(self, ai_id):
        """Delete an AI file"""
        return self.__session.delete(self.__root_url + Uri.delete_ai , data={ "token": self.__token, "ai_id": ai_id })
    
    def delete_folder(self, folder_id):
        """Delete a folder in LW"""
        return self.__session.delete(self.__root_url + Uri.delete_folder, data={ "token": self.__token, "folder_id": str(folder_id) } )


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
    
    def buy_fights(self):
        """Buy 50 fights with habs"""
        return self.__session.post(self.__root_url + Uri.buy_fights, data={'item_id':'50fights', 'quantity':1}).json()

    # Section Registre
    def get_registers(self, leek_id):
        """Get the registers of the given {leek}"""
        return self.__session.get(self.__root_url + Uri.get_registers, data={ "token": self.__token, "leek_id": leek_id }).json()

    def delete_register(self, leek_id, register_key):
        """Delete the register {key} of the given {leek}"""
        return self.__session.post(self.__root_url + Uri.delete_register, data={ "token": self.__token, "leek_id": leek_id, "key": register_key }).json()

    def set_register(self, leek_id, register_key, register_value):
        """Set the register {key} with {value} of the given {leek}"""
        return self.__session.post(self.__root_url + Uri.set_register.replace("leek_id", leek_id).replace("key", register_key).replace("value",register_value), data={ "token": self.__token}).json()

    def get_farmer_trophies(self, farmer_id):
        """Get trophies list of the given {farmer}"""
        return self.__session.get(self.__root_url + Uri.get_farmer_trophies.replace("farmer_id", farmer_id,).replace("lang","fr"), data={ "token": self.__token, "farmer_id": farmer_id, "lang":"fr"}).json()
    
    
 