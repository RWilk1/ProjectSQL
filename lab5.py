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


new_email = input('Prosze podaj email: ')
new_name = input("Podaj imie: ")
cursor.execute(f"UPDATE users SET email =? WHERE name =?", (new_email, new_name))  # Pytajnik czyli miejsce gdzie sie chce wstawic dane, pytajnik to "placeholder" na wartosci
cursor.commit()

# Commitowanie transakcji
for row in cursor.execute("SELECT * FROM users"):
    print(row)



cursor.close()
connection.close()

# SQL injection