import tkinter as tk
import csv
import os
import pandas as pd
from asyncio import streams
from msilib.schema import File
from tkinter import messagebox, ttk, filedialog
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


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
    def __init__(self, controller, csv_data_part, csv_data_all):
        super().__init__()
        self.data = csv_data_part
        self.data2 = csv_data_all
        self.controller = controller
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.back_button = tk.Button(self, text="Back", command=self.controller.back_to_doctor_view)
        self.back_button.grid(row=9, column=1, columnspan=2, padx=10, pady=5)
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)

        self.tree = ttk.Treeview(self)
        self.tree.grid(row=0, column=0, sticky='nsew')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=0, column=1, sticky='ns')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add or change patient csv_code input field label and button
        self.add_patient_label = tk.Label(self, text="Add or change patient code:")
        self.add_patient_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.add_patient_entry = tk.Entry(self)
        self.add_patient_entry.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.add_patient_button = tk.Button(self, text="Change", command=self.controller.change_patient_code)
        self.add_patient_button.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Canvas
        self.canvas = None

        # Small Frame
        self.small_frame = tk.Frame(self)
        self.small_frame.grid(row=0, column=3, padx=10, pady=5)

        self.plot_label = tk.Label(self.small_frame, text="Data plots:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)

        self.selected = tk.IntVar(value=1)
        self.boxplot_checkbox_entry = tk.Radiobutton(self.small_frame, text="Boxplot", variable=self.selected, value=1,
                                                     command=self.make_graph)
        self.matrix_checkbox_entry = tk.Radiobutton(self.small_frame, text="Age count", variable=self.selected,
                                                    value=2, command=self.make_graph)
        self.boxplot_checkbox_entry.grid(row=1, column=0, padx=10, pady=5)
        self.matrix_checkbox_entry.grid(row=1, column=1, padx=10, pady=5)

        self.make_graph()


        # Statistics
        self.stats_text = tk.Label(self, text="Please calculate some data")
        self.stats_text.grid(row=5, column=2, padx=10, pady=5)
        options = ["BMI", "Age", "MentHlth", "PhysHlth"]
        self.calculate_stats_for_combobox = tk.Button(self, text="Calculate", command=self.controller.calculate_stat)
        self.calculate_stats_for_combobox.grid(row=5, column=0, padx=10, pady=5)
        self.combo = ttk.Combobox(self, values=options)
        self.combo.set("BMI")
        self.combo.grid(row=4, column=0, padx=10, pady=5)

        # Making prediction
        self.prediction_button = tk.Button(self, text="Predict", command=self.controller.make_prediction)
        self.prediction_button.grid(row=6, column=0, padx=10, pady=5)
        self.predict_label = tk.Label(self, text="Pick patient and make prediction:")
        self.predict_label.grid(row=7, column=0, padx=10, pady=5)
        self.prediction_label = tk.Label(self, text="")
        self.prediction_label.grid(row=7, column=1, padx=10, pady=5)

    def load_columns_to_tree(self, columns):
        self.tree["columns"] = columns
        self.tree.column('#0', width=0, stretch=False)
        self.tree.heading('#0', text='', anchor="center")
        for col in columns:
            self.tree.column(col, anchor="center", width=50)
            self.tree.heading(col, text=col)

    def load_rows_to_tree(self, rows):
        data = [list(tup) for tup in rows]
        for row in data:
            self.tree.insert("", "end", values=row)

    def clear_tree(self):
        self.tree.delete(*self.tree.get_children())

    def make_graph(self):
        if self.selected.get() == 1:
            plt.clf()
            df = pd.DataFrame(self.data)
            plt.figure(figsize=(4, 2))
            sns.boxplot(data=df)
            plt.tight_layout()
            some_l = list(np.arange(df.shape[1]))
            plt.xticks(some_l, list(df.columns),
                       rotation=90, fontsize=5)
            self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
            self.canvas.get_tk_widget().grid(row=0, column=2, padx=10, pady=5)
            self.canvas.draw()
        else:
            plt.clf()
            df = pd.DataFrame(self.data2)
            plt.figure(figsize=(4, 2))
            plt.xlabel("Ages", fontsize=7)
            plt.ylabel("Count")
            sns.histplot(df)
            self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
            self.canvas.get_tk_widget().grid(row=0, column=2, padx=10, pady=5)
            self.canvas.draw()


class PatientDataManipulation(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller


class PatientDataView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.tree = ttk.Treeview(self)
        self.tree.grid(row=0, column=0, sticky='nsew')

        self.tree_data = []
            
        # Vertical scrollbar
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=0, column=1, sticky='ns')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Search input field
        self.search_label = tk.Label(self, text="Search by patient code:")
        self.search_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.search_field = tk.Entry(self)
        self.search_field.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Search button
        self.search_button = tk.Button(self, text="Search", command=self.search_data)
        self.search_button.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.checkbox_frame = tk.Frame(self)
        self.checkbox_frame.grid(row=5, column=0, padx=10, sticky="w")

        # 1 - Filter by high blood pressure
        self.high_bp_var = tk.IntVar()
        self.high_bp_checkbox = tk.Checkbutton(self.checkbox_frame, text="High Blood Pressure", variable=self.high_bp_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.high_bp_checkbox.grid(row=0, column=0, pady=3, sticky="w")
        
        # 2 - Filter by high cholesterol
        self.high_chol_var = tk.IntVar()
        self.high_chol_checkbox = tk.Checkbutton(self.checkbox_frame, text="High Cholesterol", variable=self.high_chol_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.high_chol_checkbox.grid(row=1, column=0, pady=3, sticky="w")
        
        # 3 - Filter by smoker
        self.smoker_var = tk.IntVar()
        self.smoker_checkbox = tk.Checkbutton(self.checkbox_frame, text="Smokers", variable=self.smoker_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.smoker_checkbox.grid(row=2, column=0, pady=3, sticky="w")
        
        # 4 - Filter by stroke
        self.stroke_var = tk.IntVar()
        self.stroke_checkbox = tk.Checkbutton(self.checkbox_frame, text="Had a stroke", variable=self.stroke_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.stroke_checkbox.grid(row=3, column=0, pady=3, sticky="w")
        
        # 5 - Filter by physical activity
        self.phys_activity_var = tk.IntVar()
        self.phys_activity_checkbox = tk.Checkbutton(self.checkbox_frame, text="Physically active", variable=self.phys_activity_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.phys_activity_checkbox.grid(row=4, column=0, pady=3, sticky="w")
        
        # 6 - Filter by fruits consumption
        self.fruits_var = tk.IntVar()
        self.fruits_checkbox = tk.Checkbutton(self.checkbox_frame, text="Consumes fruits", variable=self.fruits_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.fruits_checkbox.grid(row=0, column=1, sticky="w")
        
        # 7 - Filter by veggies consumption
        self.veggies_var = tk.IntVar()
        self.veggies_checkbox = tk.Checkbutton(self.checkbox_frame, text="Consumes vegetables", variable=self.veggies_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.veggies_checkbox.grid(row=1, column=1, sticky="w")
        
        # 8 - Filter by heavy alcohol consumption
        self.hvy_alcohol_consump_var = tk.IntVar()
        self.hvy_alcohol_consump_checkbox = tk.Checkbutton(self.checkbox_frame, text="Heavy alcohol consumption", variable=self.hvy_alcohol_consump_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.hvy_alcohol_consump_checkbox.grid(row=2, column=1, sticky="w")
        
        # 9 - Filter by healthcare insurance
        self.any_healthcare_var = tk.IntVar()
        self.any_healthcare_checkbox = tk.Checkbutton(self.checkbox_frame, text="Has insurance", variable=self.any_healthcare_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.any_healthcare_checkbox.grid(row=3, column=1, sticky="w")
        
        # 10 - Filter by difficulty in walking or climbing stairs
        self.diff_walk_var = tk.IntVar()
        self.diff_walk_checkbox = tk.Checkbutton(self.checkbox_frame, text="Has difficulty walking", variable=self.diff_walk_var, onvalue=1, offvalue=0, command=self.refresh_table)
        self.diff_walk_checkbox.grid(row=4, column=1, sticky="w")
        
        # Filter by sex
        self.sex_label = tk.Label(self.checkbox_frame, text="Sex:")
        self.sex_label.grid(row=0, column=2, sticky="w")

        self.sex_var = tk.StringVar(value="All")
        self.sex_combobox = ttk.Combobox(self.checkbox_frame, textvariable=self.sex_var, values=["All", "Male", "Female"])
        self.sex_combobox.grid(row=0, column=3, sticky="e")
        self.sex_combobox.bind("<<ComboboxSelected>>", self.refresh_table)
        
        # Clear filter button
        self.clear_filter_button = tk.Button(self, text="Clear filters", command=self.controller.patients_data_button)
        self.clear_filter_button.grid(row=3, column=0, padx=10, sticky="e")
        
        # Back button
        self.back_button = tk.Button(self, text="Back", command=self.controller.back_to_doctor_view)
        self.back_button.grid(row=4, column=0, padx=10, sticky="se")

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
    
    def save_data(self, tree_data):
        for item in self.tree.get_children():
            values = self.tree.item(item)['values']
            self.tree_data.append(values)

    def search_data(self):
        search_text = self.search_field.get().strip()
    
        for item in self.tree.get_children():
            first_column_value = self.tree.item(item)['values'][0]
            if str(first_column_value) != search_text:
                self.tree.delete(item)
            
    def refresh_table(self, event=None):
        self.restore_tree()

        if self.high_bp_var.get() == 1:
            for item in self.tree.get_children():
                high_bp = self.tree.item(item)['values'][1]
                if str(high_bp) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.high_chol_var.get() == 1:
            for item in self.tree.get_children():
                high_chol = self.tree.item(item)['values'][2]
                if str(high_chol) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.smoker_var.get() == 1:
            for item in self.tree.get_children():
                smoker = self.tree.item(item)['values'][5]
                if str(smoker) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.stroke_var.get() == 1:
            for item in self.tree.get_children():
                stroke = self.tree.item(item)['values'][6]
                if str(stroke) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.phys_activity_var.get() == 1:
            for item in self.tree.get_children():
                phys_activity = self.tree.item(item)['values'][8]
                if str(phys_activity) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.fruits_var.get() == 1:
            for item in self.tree.get_children():
                fruits = self.tree.item(item)['values'][9]
                if str(fruits) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.veggies_var.get() == 1:
            for item in self.tree.get_children():
                veggies = self.tree.item(item)['values'][10]
                if str(veggies) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.hvy_alcohol_consump_var.get() == 1:
            for item in self.tree.get_children():
                hvy_alcohol_consump = self.tree.item(item)['values'][11]
                if str(hvy_alcohol_consump) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.any_healthcare_var.get() == 1:
            for item in self.tree.get_children():
                any_healthcare = self.tree.item(item)['values'][12]
                if str(any_healthcare) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.diff_walk_var.get() == 1:
            for item in self.tree.get_children():
                diff_walk = self.tree.item(item)['values'][17]
                if str(diff_walk) == '0.0':
                    values = self.tree.item(item)['values']
                    self.tree.delete(item)
        if self.sex_var.get() != "All":
            if self.sex_var.get() == "Male":
                for item in self.tree.get_children():
                    sex = self.tree.item(item)['values'][18]
                    if str(sex) == '0.0':
                        values = self.tree.item(item)['values']
                        self.tree.delete(item)
            elif self.sex_var.get() == "Female":
                for item in self.tree.get_children():
                    sex = self.tree.item(item)['values'][18]
                    if str(sex) == '1.0':
                        values = self.tree.item(item)['values']
                        self.tree.delete(item)
                    
    def restore_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.tree_data:
            self.tree.insert("", "end", values=item)
            

# REFERENCES

# 0 - PatientCode : A unique code assigned to each patient.
# 1 - HighBP : Indicates if the person has been told by a health professional that they have High Blood Pressure.
# 2 - HighChol : Indicates if the person has been told by a health professional that they have High Blood Cholesterol.
# 3 - CholCheck : Cholesterol Check, if the person has their cholesterol levels checked within the last 5 years.
# 4 - BMI : Body Mass Index, calculated by dividing the persons weight (in kilogram) by the square of their height (in meters).
# 5 - Smoker : Indicates if the person has smoked at least 100 cigarettes.
# 6 - Stroke : Indicates if the person has a history of stroke.
# 7 - Diabetes : Indicates if the person has a history of diabetes, or currently in pre-diabetes, or suffers from either type of diabetes.
# 8 - PhysActivity : Indicates if the person has some form of physical activity in their day-to-day routine.
# 9 - Fruits : Indicates if the person consumes 1 or more fruit(s) daily.
# 10 - Veggies : Indicates if the person consumes 1 or more vegetable(s) daily.
# 11 - HvyAlcoholConsump : Indicates if the person has more than 14 drinks per week.
# 12 - AnyHealthcare : Indicates if the person has any form of health insurance.
# 13 - NoDocbcCost : Indicates if the person wanted to visit a doctor within the past 1 year but couldn�t, due to cost.
# 14 - GenHlth : Indicates the persons response to how well is their general health, ranging from 1 (excellent) to 5 (poor).
# 15 - Menthlth : Indicates the number of days, within the past 30 days that the person had bad mental health.
# 16 - PhysHlth : Indicates the number of days, within the past 30 days that the person had bad physical health.
# 17 - DiffWalk : Indicates if the person has difficulty while walking or climbing stairs.
# 18 - Sex : Indicates the gender of the person, where 0 is female and 1 is male.
# 19 - Age : Indicates the age class of the person, where 1 is 18 years to 24 years up till 13 which is 80 years or older, each interval between has a 5-year increment.
# 20 - Education : Indicates the highest year of school completed, with 0 being never attended or kindergarten only and 6 being, having attended 4 years of college or more.
# 21 - Income : Indicates the total household income, ranging from 1 (at least $10,000) to 6 ($75,000+)