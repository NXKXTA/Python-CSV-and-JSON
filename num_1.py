import json
import os

# Проверить файл
file_name = "./animals.json"
birds_output_file = "./birds.json"
if not os.path.exists(file_name) or not os.path.exists(birds_output_file):
    print('Неверный путь к файлу')
    exit()

# Проверка и считывание json файла
try:
    with open(file_name, "r", encoding="utf-8") as read_file:
        data_animals = json.load(read_file)
except json.decoder.JSONDecodeError:
    print("Ошибка в json файле")
    exit()

# Вывод названий птичек
data = []
for animal in data_animals["animals"]:
    if animal["animal_type"] == "Bird":
        data.append(animal)
        print(animal["name"])

# Запись птичек в файл
with open(birds_output_file, 'w') as birds_data:
    json.dump(data, birds_data, indent=4)

# Кол-во дневных животных
counter = 0
for animal in data_animals["animals"]:
    if animal["active_time"] == "Diurnal":
        counter += 1
print(f"Количество дневных животных: {counter}\n")

# Минимальный вес
weight = min([animal["weight_min"] for animal in data_animals["animals"]])
for animal in data_animals["animals"]:
    if animal["weight_min"] == weight:
        print("Животное с наименьшим весом:", animal["name"], ":", animal["weight_min"])
