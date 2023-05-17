import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


class GasEmissionData:
    def __init__(self, year: list[int], co2: list[float], ch4: list[float], n2o: list[float]):
        self.year = year
        self.co2 = co2
        self.ch4 = ch4
        self.n2o = n2o


class DataProcessor:
    @staticmethod
    def calculate_gas_emission_change(emission_data: GasEmissionData) -> dict[str, float]:
        gas_change = {"CO2": 0, "CH4": 0, "N2O": 0}

        for i in range(1, len(emission_data.year)):
            co2_change = (emission_data.co2[i] - emission_data.co2[i - 1]) / emission_data.co2[i - 1] * 100
            ch4_change = (emission_data.ch4[i] - emission_data.ch4[i - 1]) / emission_data.ch4[i - 1] * 100
            n2o_change = (emission_data.n2o[i] - emission_data.n2o[i - 1]) / emission_data.n2o[i - 1] * 100

            gas_change["CO2"] += co2_change
            gas_change["CH4"] += ch4_change
            gas_change["N2O"] += n2o_change

        gas_change["CO2"] /= len(emission_data.year) - 1
        gas_change["CH4"] /= len(emission_data.year) - 1
        gas_change["N2O"] /= len(emission_data.year) - 1

        return gas_change





class MigrationData:
    def __init__(self, immigrants: list[int], emigrants: list[int]):
        self.immigrants = immigrants
        self.emigrants = emigrants


class MigrationDataProcessor:
    @staticmethod
    def calculate_annual_migration_change(immigrants: list[int], emigrants: list[int]) -> list[float]:
        annual_change = []

        for i in range(1, len(immigrants)):
            change = ((immigrants[i] - emigrants[i]) - (immigrants[i - 1] - emigrants[i - 1])) / (
                    (immigrants[i - 1] - emigrants[i - 1]) / 2) * 100
            annual_change.append(change)

        return annual_change


class MigrationDataVisualizer:
    @staticmethod
    def plot_migration_data(immigrants: list[int], emigrants: list[int], years: list[int]):
        plt.plot(years, immigrants, label="Immigrants")
        plt.plot(years, emigrants, label="Emigrants")

        plt.xlabel("Year")
        plt.ylabel("Number of people")
        plt.title("Annual Migration")
        plt.legend()
        plt.show()


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
        file_path = self.choose_file()

        if not file_path:
            print("No file selected")
            return

        data = pd.read_csv(file_path, encoding='cp1252')
        year = data["Year"].tolist()
        co2 = data["CO2"].tolist()
        ch4 = data["CH4"].tolist()
        n2o = data["N2O"].tolist()

        gas_emission_data = GasEmissionData(year, co2, ch4, n2o)
        gas_emission_change = DataProcessor.calculate_gas_emission_change(gas_emission_data)
        print("Average annual change in greenhouse gas emissions:")
        for gas, change in gas_emission_change.items():
            print(f"{gas}: {change:.2f}%")

        DataVisualizer.plot_gas_emission_data(gas_emission_data)

    def run_migration_app(self):
        file_path = self.choose_file()

        if not file_path:
            print("No file selected")
            return

        data = pd.read_csv(file_path, encoding='cp1252')
        years = data["Year"].tolist()
        immigrants = data["Immigrants"].tolist()
        emigrants = data["Emigrants"].tolist()

        migration_data = MigrationData(immigrants, emigrants)
        annual_migration_change = MigrationDataProcessor.calculate_annual_migration_change(migration_data.immigrants,
                                                                                           migration_data.emigrants)
        print("Annual migration change:")
        for i in range(len(annual_migration_change)):
            print(f"{years[i+1]}: {annual_migration_change[i]:.2f}%")

        MigrationDataVisualizer.plot_migration_data(migration_data.immigrants, migration_data.emigrants, years)


root = tk.Tk()
app = App(master=root)
app.mainloop()