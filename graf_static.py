'''import pandas as pd
import matplotlib.pyplot as plt

class GraphicalStatistics:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Загрузка данных из файла в датафрейм"""
        self.df = pd.read_csv(self.file_path)
    
    def plot_pie_chart(self):
        """Построение круговой диаграммы расходов по типу платежной системы"""
        if self.df is None:
            raise ValueError("Данные не загружены.")
        
        # Группировка данных по 'Account Name' и суммирование расходов
        expense_data = self.df.groupby('Account Name')['Amount'].sum()
        
        plt.figure(figsize=(7, 7))
        expense_data.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title("Траты по типу платежной системы")
        plt.ylabel("")
        plt.legend (('Кредитка', 'Платиновая карта', 'Серебрянная карта'))
        plt.show()

file_path = "personal_transactions.csv"  # Путь к файлу с данными
stats = GraphicalStatistics(file_path)'''



import pandas as pd
import matplotlib.pyplot as plt
from log import log_decorator

class GraphicalStatistics:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
    
    @log_decorator()
    def load_data(self):
        """Загружает данные из файла в датафрейм"""
        self.df = pd.read_csv(self.file_path)
    
    @log_decorator()
    def plot_pie_chart(self):
        """Строит круговую диаграмму расходов по типу платежной системы"""
        if self.df is None:
            raise ValueError("Данные не загружены. Используйте load_data().")
        
        # Группируем данные по 'Account Name' и суммируем расходы
        expense_data = self.df.groupby('Account Name')['Amount'].sum()
        
        plt.figure(figsize=(7, 7))
        expense_data.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title("Траты по типу платежной системы")
        plt.ylabel("")  # Убираем подпись оси Y
        plt.show()

# Использование класса
file_path = "personal_transactions.csv"  # Укажите путь к файлу с данными
stats = GraphicalStatistics(file_path)
