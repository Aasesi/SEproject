import numpy as np
import pandas as pd
import csv

class MedicalDatabase:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.column_names_list = []
        self.rows = {}
        self.dataframe = None
        self.load_data()

    def delete(self):
        # Just normal delete function
        pass

    def insert_null(self, patient_code):
        new_data = [patient_code, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                    None, None, None, None, None, None, None]
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_data)

        # df = pd.read_csv(self.file_path)
        # new_data = {"Patient_code": patient_code, "HighBP": np.NAN, "HighChol": np.NAN, "CholCheck": np.NAN,
        #             "BMI": np.NAN, "Smoker": np.NAN, "Stroke": np.NAN, "Diabetes": np.NAN, "PhysActivity": np.NAN,
        #             "Fruits": np.NAN, "Veggies": np.NAN, "HvyAlcoholConsump": np.NAN, "AnyHealthcare": np.NAN,
        #             "NoDocbcCost": np.NAN, "GenHlth": np.NAN, "MentHlth": np.NAN, "PhysHlth": np.NAN,
        #             "DiffWalk": np.NAN,
        #             "Sex": np.NAN, "Age": np.NAN, "Education": np.NAN, "Income": np.NAN}
        # df.append(new_data, ignore_index=True)
        # df.to_csv(self.file_path, index=False)

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
            self.dataframe = df
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

    def get_rows_without_patient_code(self):
        data = self.dataframe.drop(["Patient_code", "Sex", "HighBP", "HighChol", "CholCheck", "Stroke",
                                    "DiffWalk", "Smoker", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump",
                                    "AnyHealthcare", "NoDocbcCost"], axis=1)
        return data

    def get_specific_column_data(self, name):
        column_name_data = [item[name] for item in self.rows]
        return column_name_data
