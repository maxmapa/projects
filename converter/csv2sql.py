import pandas as pd
import sqlite3

# Задайте шлях до вашого CSV файлу
csv_file_path = 'converter\\2024_part1.csv'

# Задайте назву бази даних SQLite
db_file_path = 'converter\\att2024.db'

# Задайте назву таблиці в базі даних
table_name = 'bookings'

# Читаємо CSV файл у DataFrame, вказуємо розділювач колонок
df = pd.read_csv(csv_file_path, sep=';')

# Створюємо SQLite підключення
conn = sqlite3.connect(db_file_path)

# Конвертуємо DataFrame у SQLite таблицю
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Закриваємо підключення до бази даних
conn.close()

print("CSV файл успішно конвертовано в базу даних SQLite.")
