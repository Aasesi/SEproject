from MedicalDatabase import MedicalDatabase
from UsersDatabase import UserDatabase


class System:
    def __init__(self):
        self.patient_database = MedicalDatabase("Nofileyet")
        self.current_user = None
        self.user_database = UserDatabase("Accounts.txt")

    def register(self, name, surname, role, username, password):
        self.user_database.add_user(name, surname, role, username, password)

    def login(self, username, password):
        if self.user_database.user_exists(username, password):
            self.current_user = self.user_database.get_user(username)
            return True
        else:
            return False

    def delete_user(self):
        pass

    def get_statistical_results(self):
        pass

    def access_database(self):
        pass
