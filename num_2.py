import csv
import os

countries_input_path = "./countries.csv"
countries_output_path = "./countries_output.csv"
inflation_path = "./inflation.csv"
if not all(
        [os.path.exists(countries_input_path), os.path.exists(countries_output_path), os.path.exists(inflation_path)]):
    print("Неверный путь к файлу")
    exit()

try:
    first_x = int(input("Введите 1ю границу диапазона: "))
    second_x = int(input("Введите 2ю границу диапазона: "))
except ValueError:
    print("Неверно введён диапазон")
    exit()

countries = []
with open(countries_input_path, 'r', encoding="utf-8") as input_csvfile:
    reader = csv.reader(input_csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    next(reader)  # Пропускаем первую строку (заголовки столбцов)
    titles = list(reader)

# Запись стран из диапазона
data = []
for row in titles:
    if min(first_x, second_x) <= int(row[2]) <= max(first_x, second_x):
        data.append(row)
with open(countries_output_path, 'w', newline='') as file:
    writer = csv.writer(file)  # Создание объекта writer
    writer.writerows(data)  # Запись списка списков в файл CSV

sorted_countries = sorted(titles, key=lambda x: x[-2])
with open(inflation_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_countries)
