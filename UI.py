import tkinter as tk
from tkinter import filedialog

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_gas_emission_button = tk.Button(self)
        self.select_gas_emission_button["text"] = "Анализ выбросов газов"
        self.select_gas_emission_button["command"] = self.run_gas_emission_app
        self.select_gas_emission_button.pack(side="top")

        self.select_migration_button = tk.Button(self)
        self.select_migration_button["text"] = "Анализ миграции населения"
        self.select_migration_button["command"] = self.run_migration_app
        self.select_migration_button.pack(side="top")

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        return file_path

    def run_gas_emission_app(self):
        # Этот метод должен быть переопределен в дочернем классе
        pass

    def run_migration_app(self):
        # Этот метод должен быть переопределен в дочернем классе
        pass

root = tk.Tk()
app = App(master=root)
app.mainloop()