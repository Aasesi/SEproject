import csv
import pandas as pd


class MedicalDatabase:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.column_names_list = []
        self.rows = {}

    def delete(self):
        # Just normal delete function
        pass

    def insert(self):
        # Insert patient data. Two cases(optional btw we can just add entire row) one for inserting entire row and one
        # for updating/insert (maybe adding missing data to some patient)
        pass

    def interpret_data(self):
        # I do not remember why we have this
        pass

    def correct_data(self):
        # Correct missing value if any. I think we can make it initialized by click of the button.
        pass

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path)
            self.column_names_list = df.columns.tolist()
            self.rows = df.to_dict(orient="records")
            return True
        except FileNotFoundError:
            return False

    def save_data(self):
        # Saves data to file. Something should be in parameters
        pass

    def get_column_names(self):
        return self.column_names_list

    def get_rows(self):
        return self.rows
