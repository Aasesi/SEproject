import tkinter as tk
from tkinter import messagebox


class LoginView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.controller.login)
        self.sign_up_button = tk.Button(self, text="Sign up", command=self.controller.go_to_sign_up)

        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.sign_up_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)


class MainView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)


class RegisterView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.name_label = tk.Label(self, text="Name:")
        self.name_entry = tk.Entry(self)
        self.surname_label = tk.Label(self, text="Surname:")
        self.surname_entry = tk.Entry(self)
        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.user_type_label = tk.Label(self, text="User type:")
        self.register_button = tk.Button(self, text="Register", command=self.controller.register_account)
        self.back_button = tk.Button(self, text="Back", command=self.controller.start)

        self.selected = tk.IntVar()
        self.doctor_checkbox_entry = tk.Radiobutton(self, text="Doctor", variable=self.selected, value=1)
        self.patient_checkbox_entry = tk.Radiobutton(self, text="Patient", variable=self.selected, value=2)

        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.surname_label.grid(row=1, column=0, padx=10, pady=5)
        self.surname_entry.grid(row=1, column=1, padx=10, pady=5)
        self.username_label.grid(row=2, column=0, padx=10, pady=5)
        self.username_entry.grid(row=2, column=1, padx=10, pady=5)
        self.password_label.grid(row=3, column=0, padx=10, pady=5)
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)
        self.user_type_label.grid(row=4, column=0, padx=10, pady=5)
        self.doctor_checkbox_entry.grid(row=4, column=1, padx=10, pady=5)
        self.patient_checkbox_entry.grid(row=4, column=2, padx=10, pady=5)
        self.register_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.back_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)


class DoctorMenuView(tk.Frame):
    def __init__(self, controller, name: str, surname: str):
        super().__init__()
        self.controller = controller
        self.name_label = tk.Label(self, text=f"{name}")
        self.surname_label = tk.Label(self, text=f"Surname: {surname}")
        self.data_analysis_button = tk.Button(self, text="Data Analysis",
                                              command=self.controller.data_analysis_button)
        self.patients_button = tk.Button(self, text="Patients Data", command=self.controller.data_analysis_button)
        self.logout_button = tk.Button(self, text="Logout", command=self.controller.start)

        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.surname_label.grid(row=0, column=1, padx=10, pady=5)
        self.data_analysis_button.grid(row=1, column=0, padx=10, pady=5)
        self.patients_button.grid(row=2, column=0, padx=10, pady=5)
        self.logout_button.grid(row=3, column=0, padx=10, pady=5)
