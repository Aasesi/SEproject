import tkinter as tk
import csv
import os
import pandas as pd
from asyncio import streams
from msilib.schema import File
from tkinter import messagebox, ttk, filedialog


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
        self.patients_button = tk.Button(self, text="Patients Data", command=self.controller.patients_data_button)
        self.logout_button = tk.Button(self, text="Logout", command=self.controller.start)

        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.surname_label.grid(row=0, column=1, padx=10, pady=5)
        self.data_analysis_button.grid(row=1, column=0, padx=10, pady=5)
        self.patients_button.grid(row=2, column=0, padx=10, pady=5)
        self.logout_button.grid(row=3, column=0, padx=10, pady=5)


class PatientView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)


class DataAnalysisView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.back_button = tk.Button(self, text="Back", command=self.controller.back_to_doctor_view)
        self.back_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)


class PatientDataManipulation(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)


class PatientDataView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.tree = ttk.Treeview(self)
        self.tree.grid(row=0, column=0, sticky='nsew')

        # Vertical scrollbar
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=0, column=1, sticky='ns')

        # Horizontal scrollbar (To be removed (probably))
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=hsb.set)
        hsb.grid(row=1, column=0, sticky='ew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Search input field
        self.search_field = tk.Entry(self)
        self.search_field.grid(row=2, column=0, padx=10, pady=5)

        # Search button
        self.search_button = tk.Button(self, text="Search", command=self.search_data)
        self.search_button.grid(row=3, column=0, padx=10, pady=5)
        
        # Clear filter button
        self.clear_filter_button = tk.Button(self, text="Clear filter", command=self.controller.patients_data_button)
        self.clear_filter_button.grid(row=4, column=0, padx=10, pady=5)
        
        # Back button
        self.back_button = tk.Button(self, text="Back", command=self.controller.back_to_doctor_view)
        self.back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def load_columns_to_tree(self, columns):
        self.tree["columns"] = columns
        self.tree.column('#0', width=0, stretch=False)
        self.tree.heading('#0', text='', anchor="center")
        for col in columns:
            self.tree.column(col, anchor="center", width=50)
            self.tree.heading(col, text=col)

    def load_rows_to_tree(self, rows):
        columns = list(rows[0].keys())
        for item in rows:
            values = [item[column] for column in columns]
            self.tree.insert("", "end", values=values)
    
    def search_data(self):
        search_text = self.search_field.get().strip()
    
        for item in self.tree.get_children():
            first_column_value = self.tree.item(item)['values'][0]
            if str(first_column_value) != search_text:
                self.tree.delete(item)