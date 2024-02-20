from MedicalDatabase import MedicalDatabase
from UsersDatabase import UserDatabaseSQL
from User import User
from DataAnalysis import DataAnalysis
import pandas as pd


class System:
    def __init__(self):
        self.patient_database = MedicalDatabase("csvFiles/patients_data.csv")
        self.current_user = None
        self.user_database = UserDatabaseSQL()
        self.user_database.create_table()
        self.data_analysis = DataAnalysis()

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

    def get_user_database(self):
        data = [("Username", "Name", "Surname", "Patient_Csv_code"), self.user_database.get_users()]
        return data

    def change_patient_code(self, username, code):
        code_in_string = str(code)
        if code_in_string:
            self.user_database.assign_csv_code(username, code_in_string)
            return True
        else:
            return False

    def access_database(self):
        pass

    def get_part_of_csv(self):
        return [self.patient_database.get_rows_without_patient_code(), self.patient_database.get_rows()]

    def calculate_data_for(self, name):
        data = self.patient_database.get_specific_column_data(name)
        data_list = [self.data_analysis.calculate_median(data), self.data_analysis.calculate_average(data),
                     self.data_analysis.calculate_variance(data), self.data_analysis.calculate_mode(data),
                     self.data_analysis.standard_deviation(data)]
        return data_list

    def prediction_making(self, row_code):
        data = self.patient_database.get_rows()
        for
        df = pd.DataFrame(data)
        specific_row_data = df[df["Patient_code"] == row_code]
        self.data_analysis.train_model_heart_disease()
        prediction = self.data_analysis.predict(specific_row_data)
        print(prediction)
