# baza sql w pythonie
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # sql_connection = sqlite3.connect(':memory:')  # baza umieszczona w pamięci
    cursor = sql_connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS sqliteDB_developers (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_data DATETIME,
    salary REAL NOT NULL);
    '''

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    # uruchamiamy query
    # cursor.execute(query)
    # sql_connection.commit()

    # uruchamiamy skrypt sql
    cursor.executescript(sql_script)

    print("Baza danch została podłaczona")
except sqlite3.Error as e:
    print("Bład otwierania bazy danch", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
