# Laczenie sie z bazami danych
from dotenv import load_dotenv
import os
import pyodbc
import datetime as dt

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
# cursor = connection.cursor()

# CREATE TABLE accounts
# (
# 	Acc_id INT IDENTITY PRIMARY KEY,
# 	account_name VARCHAR(100)	NOT NULL,
# 	account_balance FLOAT		NOT NULL
# )

# CREATE TABLE Transactions (
#     transaction_id INT IDENTITY PRIMARY KEY,
#     account_id  INT FOREIGN KEY REFERENCES accounts,
#     transaction_tim DATETIME,
#     amount FLOAT NOT NULL
# )



######################################################################
class Account:

    @staticmethod
    def current_time():
        return dt.datetime.now()

    def __init__(self, name: str, open_balance: float = 0.0):
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO accounts (account_name, account_balance) VALUES (?,?)', (name, open_balance))
            cursor.execute("SELECT @@IDENTITY AS ID")   # ostatnie wygenerowane ID
            self.id = cursor.fetchone()[0]
            self.name = name
            self._balance = open_balance
            print(f"Account {name} was created with open balance {round(open_balance,2)}, id={self.id}")
    def deposit(self, amount: float, commit=True):
        if amount < 0:
            raise ValueError("Wrong amount to deposit")
            cursor = connection.cursor()
        try:
            # with connection.cursor() as cursor:

            self._balance += amount
            cursor.execute("UPDATE accounts SET account_balance = ? WHERE Acc_id = ?", (self._balance, self.id))
            cursor.execute("INSERT INTO transactions (account_id, transaction_time, amount) VALUES (?,?,?)", (self.id, Account.current_time(), amount))
            print(f"amount {amount} deposit to account {self.name}")
        if commit=True:

            cursor.commit()
    def withdraw(self, amount: float, commit=True):
        if amount < 0 or amount > self._balance:
            raise ValueError("Wrong amount to withdraw")
        cursor = connection.cursor()
        try:
            # with connection.cursor() as cursor:
            self._balance -= amount
            cursor.execute("UPDATE accounts SET account_balance = ? WHERE Acc_id = ?", (self._balance, self.id))
            cursor.execute("INSERT INTO transactions (account_id, transaction_time, amount) VALUES (?,?,?)",(self.id, Account.current_time(), amount))
            print(f"{amount} withraw from account {self.name}")
            if commit:
                cursor.commit()
        except Exception:
            cursor.commit()
    def show_balance(self):
        print(f"Account {self.name} balance: {self._balance}")



# Metoda "ogolnodostepna"
def do_transaction(account_from: Account, account_to: Account, amount: float):
    if  account._balance >= amount:
        account_from.withdraw(amount)
        account_to.deposit(amount)
    else:
        exit()



if __name__ == '__main__':
    account = Account('Andrzej', 100)
    account2 = Account('Maciej', 50)
    do_transaction(account2, account, amount=51)

    # account.deposit(10)
    # account.deposit(0.1)
    # account.deposit(0.3)
    # account.deposit(7.2)
    # account.withdraw(7.2)
    # account.show_balance()






# load_dotenv()
# database_password = os.environ.get("DATABASE_PASSWORD")
# # print(database_password)
# database_server = 'morfeusz.wszib.edu.pl'
# driver = "ODBC Driver 18 for SQL Server"
# database_user = 'rawilk'
# database_name = 'rawilk'
#
# # 1) Utworzenie connection-string-a
# connection_string = f'Driver={driver};' \
#                     f'SERVER={database_server};' \
#                     f'DATABASE={database_name};' \
#                     f'UID={database_user};'\
#                     f'PWD={database_password};' \
#                     'Encrypt=no;'
# connection = pyodbc.connect(connection_string)
# cursor = connection.cursor()
#
#
# new_email = input('Prosze podaj email: ')
# new_name = input("Podaj imie: ")
# cursor.execute(f"UPDATE users SET email =? WHERE name =?", (new_email, new_name))  # Pytajnik czyli miejsce gdzie sie chce wstawic dane, pytajnik to "placeholder" na wartosci
# cursor.commit()
#
# # Commitowanie transakcji
# for row in cursor.execute("SELECT * FROM users"):
#     print(row)
#
#
#
# cursor.close()
# connection.close()

# SQL injection