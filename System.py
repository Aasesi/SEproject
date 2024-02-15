from MedicalDatabase import MedicalDatabase
from UsersDatabase import UserDatabaseSQL
from User import User


class System:
    def __init__(self):
        self.patient_database = MedicalDatabase("csvFiles/patients_data")
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

    def get_database_data(self):
        if self.patient_database.load_data():
            csv_data = [self.patient_database.get_column_names(), self.patient_database.get_rows()]
            return csv_data
        else:
            return []

    def access_database(self):
        pass
