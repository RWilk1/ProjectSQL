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
# these all undermentioned statemants are the start of transaction
# wszystkie zapytania, które modyfikukja dane to otwarcie nowej transakcji
cursor = connection.cursor()

# connection.execute("DROP TABLE users")
# connection.execute("CREATE TABLE users (id int identity, name varchar(100), age int)")
connection.execute("INSERT INTO users (name, age) VALUES('Rafal',20), ('Iza', 30)")

# Commitowanie transakcji
cursor.commit()

# Otwarcie nowej transakcji bez commitowania
connection.execute("INSERT INTO users (name, age) VALUES('x',20)")

for row in cursor.execute("SELECT * FROM users"):
    print(row)




# cursor.execute("SELECT * FROM users")
# results = cursor.fetchall()
# results2 = cursor.fetchone()
# results3 = cursor.fetchmany(1)
# print(results)
# print(results2)
# print(results3)

# typ danych krotka
# for row in cursor:
#     print(row)
# for id, name, age in cursor:
#     print(id, name, age)
# for row in cursor.execute("SELECT * FROM users"):
#     print(row)
#
# # Zamykanie połączenia i kursora
# print(cursor.connection)
#
# cursor.execute("SELECT * FROM users")
# # for row in results3:
# #     print(row)
cursor.close()
connection.close()
