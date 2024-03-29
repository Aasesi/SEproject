from Frames import *
from tkinter import messagebox


class View:
    def __init__(self):
        self.current_frame = None
        self.controller = None
        self.temp_data = []
        self.patient_data = []

    def switch(self, name):
        if self.current_frame is not None:
            self.current_frame.destroy()
        if name == "Login":
            self.current_frame = LoginView(self.controller)
            self.current_frame.pack_propagate(False)
            self.current_frame.place(relx=.5, rely=.3, anchor="center")
        if name == "Register":
            self.current_frame = RegisterView(self.controller)
            self.current_frame.pack_propagate(False)
            self.current_frame.place(relx=.5, rely=.3, anchor="center")
        if name == "DoctorViewMain":
            self.current_frame = DoctorMenuView(self.controller, self.temp_data[0], self.temp_data[1])
            self.current_frame.pack_propagate(False)
            self.current_frame.place(relx=.5, rely=.3, anchor="center")
        if name == "PatientView":
            self.current_frame = PatientView(self.controller, self.patient_data)
            self.current_frame.pack_propagate(False)
            self.current_frame.place(relx=.5, rely=.3, anchor="center")
        if name == "DataAnalysisView":
            self.current_frame = DataAnalysisView(self.controller, self.temp_data[0], self.temp_data[1])
            self.current_frame.pack_propagate(False)
            self.current_frame.place(relx=.5, rely=.3, anchor="center")
        if name == "PatientDataManipulation":
            self.current_frame = PatientDataManipulation(self.controller)
            self.current_frame.pack_propagate(False)
            self.current_frame.place(relx=.5, rely=.3, anchor="center")
        if name == "PatientDataView":
            self.current_frame = PatientDataView(self.controller)
            self.current_frame.pack_propagate(False)
            self.current_frame.place(relx=.5, rely=.3, anchor="center")

    def give_temp_data(self, temp_list):
        self.temp_data = temp_list
        
    def pass_patient_data(self, data):
        self.patient_data = data

    def set_controller(self, controller):
        self.controller = controller

    def get_current_frame(self):
        return self.current_frame

    def show_message_box(self):
        messagebox.showinfo("Info", "Incorrect username or password")

    def show_message(self):
        messagebox.showinfo("Incorrect", "Patient not selected in data!!!")
