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
        if self.model.login(user, password):
            if self.model.current_user.userType == "Doctor":
                temp_data = [self.model.current_user.name, self.model.current_user.surname]
                self.view.give_temp_data(temp_data)
                self.view.switch("DoctorViewMain")
            else:
                self.view.switch("PatientView")

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
        self.view.switch("DataAnalysisView")

    def patient_data_manipulation(self):
        self.view.switch("PatientDataManipulation")

    def patients_data_button(self):
        self.view.switch("PatientDataView")