import csv

# Имя файла, в котором нужно искать записи
file_name = r"C:\My_files\Anothers\Talisman\12.csv"
# Имя выходного файла c найденными записями Excel
output_file_name = "output.xlsx"

# Определение целевых значений для поиска
target_status = "Договор"
target_total_amount = 0

# Создание пустого списка для найденных записей
found_records = []
count = 0
# Открытие файла и чтение его содержимого
with open(file_name, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Проверка значений столбцов
        if row["Статус сделки"] == target_status and float(row["Общая сумма"]) == target_total_amount:
            found_records.append(row)
        count += 1
    print(count)

# Вывод найденных записей
if found_records:
    print("Найденные записи:")
    for record in found_records:
        print(record)
else:
    print("Записи, соответствующие заданным критериям, не найдены.")

