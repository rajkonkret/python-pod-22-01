# baza sql w pythonie
import sqlite3

data = [
    (11, 'Python', 2000.0),
    (12, 'Tomek', 3500.0),
    (13, 'Zebnek', 4589.0)
]
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danch została podłaczona")
    insert = '''
    INSERT INTO software (id,name,price) VALUES (1,'Python', 200);
    '''

    insert2 = '''
    INSERT INTO software (id,name,price) VALUES (?,?,?);
    '''

    insert_many = '''
    INSERT INTO software (id,name,price) VALUES (?,?,?);
    '''

    select = '''
    SELECT * FROM SOFTWARE WHERE id=1;
    '''

    select_all = '''
    SELECT * FROM SOFTWARE;
    '''

    delete = '''
    DELETE FROM software WHERE id=1;
    '''

    update = '''
    UPDATE software SET price=2000 WHERE id=1;
    '''

    # insert
    # cursor.execute(insert)
    # sql_connection.commit()

    # insert2
    # cursor.execute(insert2, ("2", 'Tomek', 3500))
    # sql_connection.commit()

    id = 3
    name = "Zebnek"
    price = 4589
    # # insert2
    # cursor.execute(insert2, (id, name, price))
    # sql_connection.commit()

    # insert many
    cursor.executemany(insert_many, data)
    sql_connection.commit()

    # delete
    # cursor.execute(delete)
    # sql_connection.commit()

    # update
    cursor.execute(update)
    sql_connection.commit()  # (1, 'Python', 2000.0)

    # select
    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 200.0)

    for row in cursor.execute(select_all):
        print(row)  # (1, 'Python', 200.0)


except sqlite3.Error as e:
    print("Bład otwierania bazy danch", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
