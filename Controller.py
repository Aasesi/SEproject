from View import View
from System import System


class Controller:
    def __init__(self, view, model):
        self.view: View = view
        self.model: System = model

    def start(self):
        self.view.switch("Login")

    def login(self):
        user = user = self.view.get_current_frame().username_entry.get()
        password = self.view.get_current_frame().password_entry.get()
        if self.model.login(user, password):
            self.view.switch("MainView")
        else:
            self.view.show_message_box()

    def go_to_sign_up(self):
        self.view.switch("Register")

    def register_account(self):
        user = self.view.get_current_frame().username_entry.get()
        password = self.view.get_current_frame().password_entry.get()
        name = self.view.get_current_frame().name_entry.get()
        surname = self.view.get_current_frame().surname_entry.get()
        user_type = self.view.get_current_frame().user_type_entry.get()
        self.model.register(name, surname, user_type, user, password)
