# baza sql w pythonie
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danch została podłaczona")
except sqlite3.Error as e:
    print("Bład otwierania bazy danch", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
