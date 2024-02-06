from MedicalDatabase import MedicalDatabase
from UsersDatabase import UserDatabaseSQL
from User import User


class System:
    def __init__(self):
        self.patient_database = MedicalDatabase("Nofileyet")
        self.current_user = None
        self.user_database = UserDatabaseSQL()
        self.user_database.create_table()

    def register(self, name, surname, role, username, password):
        self.user_database.add_user(name, surname, role, username, password)

    def login(self, username, password):
        if self.user_database.validate(username, password) != 0:
            user_data = self.user_database.get_current_user(username, password)
            for r in user_data:
                print(r)
            self.current_user = User(user_data[0][0], user_data[0][1], user_data[0][2])
            return True
        else:
            return False

    def delete_user(self):
        pass

    def get_statistical_results(self):
        pass

    def access_database(self):
        pass
