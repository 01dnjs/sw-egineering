import json


class UserData:

    def __init__(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            self.__user_data : dict = json.load(file)
    
    def id_check(self, id):
        return id in self.__user_data
    
    def password_check(self, id, password):
        return self.__user_data[id] == password
    
    def save(self, path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.__user_data, file)

    def add_user(self, id, props):
        if id not in self.__user_data:
            self.__user_data[id] = props
            return True
        else:
            return False
        
    def modify_prop(self, id, prop, val):
        if id in self.__user_data:
            self.__user_data[id][prop] = val
            return True
        else:
            return False
    
    def delete_user(self, id):
        if id in self.__user_data:
            del self.__user_data[id]
        
    def get_user_prop(self, id, prop):
        if id in self.__user_data:
            return self.__user_data[id][prop]
        else:
            return None