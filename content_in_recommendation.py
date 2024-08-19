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
invalid_records = []
invalid_rows_count = 0
without_recomendation = []
valid_rows_count = 0
column = "Последняя рекомендация"
# Открытие файла и чтение его содержимого
with open(file_name, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Проверка значений столбцов
        if "23/24" in row[column] or "24/25" in row[column]:
            found_records.append(row)
            valid_rows_count += 1
        else:
            if len(row[column]) > 0:
                fio = row["ФИО"]
                rec = row[column]
                deal = row['Сделка']
                status = row['Статус сделки']
                summ_pay = row['Общая сумма']
                client = {"FIO": fio, "R": rec, "Deal": deal, "Status": status, "Summ_pay": summ_pay}
                invalid_records.append(client)
                invalid_rows_count += 1
            else:
                without_recomendation.append(row[column])

# Вывод найденных невалидных записей
if invalid_records:
    for i in invalid_records:
        print(i['FIO'], i["R"], i['Deal'])
print(f"\nКоличество потенциально невалидных записей:\n{invalid_rows_count}")
