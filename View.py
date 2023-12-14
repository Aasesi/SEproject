from Frames import LoginView, RegisterView, MainView
from tkinter import messagebox


class View:
    def __init__(self):
        self.current_frame = None
        self.controller = None

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
        if name == "MainView":
            self.current_frame = MainView(self.controller)
            self.current_frame.pack_propagate(False)
            self.current_frame.place(relx=.5, rely=.3, anchor="center")

    def set_controller(self, controller):
        self.controller = controller

    def get_current_frame(self):
        return self.current_frame

    def show_message_box(self):
        messagebox.showinfo("some info", "hello")
