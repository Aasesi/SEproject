from View import View
from System import System


class Controller:
    def __init__(self, view, model):
        self.view: View = view
        self.model: System = model

    def start(self):
        self.view.switch("Login")

    def login(self):
        user = self.view.get_current_frame().username_entry.get()
        password = self.view.get_current_frame().password_entry.get()
        if user.isdigit():
            data = self.model.get_data()
            if self.find_patient_record(data, user):
                self.view.pass_patient_data(self.find_patient_record(data, user))
                self.view.switch("PatientView")
            else:
                self.view.show_message()
        else:
            if self.model.login(user, password):
                temp_data = [self.model.current_user.name, self.model.current_user.surname]
                self.view.give_temp_data(temp_data)
                self.view.switch("DoctorViewMain")
            else:
                self.view.show_message_box()

    def go_to_sign_up(self):
        self.view.switch("Register")

    def register_account(self):
        user = self.view.get_current_frame().username_entry.get()
        password = self.view.get_current_frame().password_entry.get()
        name = self.view.get_current_frame().name_entry.get()
        surname = self.view.get_current_frame().surname_entry.get()
        user_type = "Patient"
        if self.view.get_current_frame().selected.get() == 1:
            user_type = "Doctor"
        self.model.register(name, surname, user_type, user, password)

    def data_analysis_button(self):
        data = self.model.get_part_of_csv()
        self.view.give_temp_data(data)
        self.view.switch("DataAnalysisView")
        data = self.model.get_user_database()
        self.view.get_current_frame().load_columns_to_tree(data[0])
        self.view.get_current_frame().load_rows_to_tree(data[1])

    def patient_data_manipulation(self):
        self.view.switch("PatientDataManipulation")

    def change_patient_code(self):
        selected_item = self.view.get_current_frame().tree.focus()
        if selected_item:
            code = self.view.get_current_frame().add_patient_entry.get()
            username = self.view.get_current_frame().tree.item(selected_item, 'values')[0]
            self.model.change_patient_code(username, code)
            self.model.insert_data_to_csv(code)
            self.view.get_current_frame().clear_tree()
            data = self.model.get_user_database()
            self.view.get_current_frame().load_columns_to_tree(data[0])
            self.view.get_current_frame().load_rows_to_tree(data[1])
        else:
            self.view.show_message()

    def patients_data_button(self):
        self.view.switch("PatientDataView")
        data = self.model.get_database_data()
        self.view.get_current_frame().load_columns_to_tree(data[0])
        self.view.get_current_frame().load_rows_to_tree(data[1])
        self.view.get_current_frame().save_data(self.view.get_current_frame().tree_data)
        
    def find_patient_record(self, patient_data, patient_code):
        for record in patient_data:
            if str(record['Patient_code']) == patient_code:
                return record
        return None

    def back_to_doctor_view(self):
        temp_data = [self.model.current_user.name, self.model.current_user.surname]
        self.view.give_temp_data(temp_data)
        self.view.switch("DoctorViewMain")

    def calculate_stat(self):
        selected = self.view.get_current_frame().combo.get()
        data = self.model.calculate_data_for(selected)
        self.view.get_current_frame().stats_text.config(text=f"Median = {data[0]}\nAverage = {data[1]}\nVariance = "
                                                             f"{data[2]}\n Mode = {data[3]}\n Standard deviation"
                                                             f" = {data[4]}")

    def make_prediction(self):
        selected_item = self.view.get_current_frame().tree.focus()
        if selected_item:
            self.view.show_message_box()
        else:
            self.view.show_message()
