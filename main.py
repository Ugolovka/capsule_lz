from graf_static import GraphicalStatistics


file_path = "personal_transactions.csv"  # Путь к файлу с данными
stats = GraphicalStatistics(file_path)
print(stats.load_data())
print(stats.plot_pie_chart())