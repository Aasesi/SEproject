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
        self.csv_file = 'csvFiles\\heart_disease_health_indicators_BRFSS2015.csv'

        # Create a Treeview
        self.tree = ttk.Treeview(self)
        self.tree.grid(row=1, column=0, padx=10, pady=5)

        # Add columns to the Treeview
        self.tree["columns"] = ("#0", *self.get_column_names())
        self.columns = self.tree["columns"]

        # Column headings
        self.tree.heading("#0", text="Index")
        for i, col in enumerate(self.get_column_names(), start=1):
            self.tree.heading(f"#{i}", text=col)

        for col in self.columns:
            self.tree.column(col, width=50)

        # Display the first 100 records
        self.display_records()

        # Vertical scrollbar
        self.v_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.v_scrollbar.grid(row=1, column=1, sticky="E")
        self.tree.configure(yscrollcommand=self.v_scrollbar.set)

        # Horizontal scrollbar
        self.h_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.h_scrollbar.grid(row=2, column=0, sticky="S")
        self.tree.configure(xscrollcommand=self.h_scrollbar.set)

    def get_column_names(self):
        try:
            df = pd.read_csv(self.csv_file)
            return df.columns.tolist()
        except FileNotFoundError:
            messagebox.showerror("Error", "CSV file not found.")
            return []

    def display_records(self):
        try:
            df = pd.read_csv(self.csv_file)

            # Display first 100 records
            for index, row in df.head(100).iterrows():
                self.tree.insert("", "end", text=index, values=row.tolist())

        except FileNotFoundError:
            messagebox.showerror("Error", "CSV file not found.")