import pyodbc

for d in pyodbc.drivers():
    print(d)