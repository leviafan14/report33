import csv
from request_recomendation import send_get_request, url, access_token

# Имя файла, в котором нужно искать записи
file_name = r"C:\My_files\Anothers\Talisman\rawr1.csv"
# Имя выходного файла c найденными записями Excel
output_file_name = "output.xlsx"

# Определение целевых значений для поиска
target_status = "Бронь"
target_total_amount = 0

# Создание пустого списка для найденных записей
found_records = []
invalid_records = []
invalid_rows_count = 0
without_recomendation = []
valid_rows_count = 0
column = "Сделка"

# Открытие файла и чтение его содержимого
with open(file_name, "r", encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Получение записей у которых поле Сделка заполнено
        if len(row[column]) > 0:
            found_records.append({"FIO": row["ФИО"], "Deal_ID": row[column]})
            valid_rows_count += 1

# Вывод количества найденных записей
print(f"\nКоличество записей с непустым полем Сделка:\n{len(found_records)}")

deals_with_date = []
deals_invalid_date = []
invalid_users_count = 0
if found_records:
    for i in found_records:
        inserted_at = send_get_request(url, i['Deal_ID'], access_token)
        if "2024" in str(inserted_at):
            deals_with_date.append({"FIO": i["FIO"], "Deal": i['Deal_ID'], 'Date': inserted_at})
        else:
            deals_invalid_date.append({"FIO": i["FIO"], "Deal": i['Deal_ID'], 'Date': inserted_at})
            invalid_users_count += 1
            print(invalid_users_count)
print(deals_invalid_date, f"\n Количество невалидных записей: {invalid_users_count}")
