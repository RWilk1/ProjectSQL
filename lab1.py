print("Hi")

# Laczenie sie z bazami danych

from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()
database_password = os.environ.get("DATABASE_PASSWORD")
print(database_password)
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
connection.execute("CREATE TABLE users (id int identity, name varchar(100), age int)")
connection.execute("INSERT INTO users (name, age) VALUES('Rafal',20), ('Iza', 30)")

# Obiekt kursor, sluzy do obslugiwania baz danych, jest to obiekt ktory iteruje tabele danych linia po lini
# Ten kursor dziala po stronie servera, a nie klienta
cursor = connection.cursor()
cursor.execute("SELECT * FROM users")

# typ danych krotka
# for row in cursor:
#     print(row)
for id, name, age in cursor:
    print(id, name, age)

# Zamykanie połączenia i kursora
print(cursor.connection)
cursor.close()
connection.close()
