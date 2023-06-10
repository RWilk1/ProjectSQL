# Laczenie sie z bazami danych
from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()
database_password = os.environ.get("DATABASE_PASSWORD")
# print(database_password)
database_server = 'morfeusz.wszib.edu.pl'
driver = "ODBC Driver 18 for SQL Server"
database_user = 'rawilk'
database_name = 'rawilk'

# 1) Utworzenie connection-string-a
connection_string = f'Driver={driver};' \
                    f'SERVER={database_server};' \
                    f'DATABASE={database_name};' \
                    f'UID={database_user};'\
                    f'PWD={database_password};' \
                    'Encrypt=no;'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()


new_name = input("Podaj imie: ")
sql = f"UPDATE users SET email='test@test' WHERE name ='{new_name}'"
split_arr = sql.split(';')

for update in split_arr:
    cursor.execute(update)

cursor.commit()

cursor.close()
connection.close()

# SQL injection