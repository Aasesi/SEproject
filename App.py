import tkinter as tk
from System import System
from Controller import Controller
from View import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical statistics database")
        self.geometry('1200x800')
        model = System()
        view = View()
        self.controller = Controller(view, model)
        view.set_controller(self.controller)
        self.controller.start()
