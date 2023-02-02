"""
data_generator.py is a Python file that generates random coordinates (t, y) with the frequency
of <frequency>, and it stores these coordinates in a SQLite database which is created in the
path of <pathOfDb>. The t value in a coordinate stands for the time, and the y value stands for
a random float between the <low> and <high> variables.
"""

import numpy as np
import time
import sqlite3


def coordinate_generator(low, high):
    """Generates random coordinates between low and high"""
    x = time.time() - startTime
    y = low + np.random.random() * (high - low)
    return x, y


def create_connection(path):
    """Creates a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("SQLite3 " + str(sqlite3.version))

    except sqlite3.Error as e:
        print(e)

    finally:
        if conn:
            return conn


def create_coordinate_table(conn):
    """Creates a coordinate table in a SQLite database"""
    query = """CREATE TABLE IF NOT EXISTS coordinates (ID INT, x FLOAT, y FLOAT);"""
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except sqlite3.Error as e:
        print(e)


def insert_coordinate(conn, id, coordinate):
    """Inserts a coordinate to a SQLite database"""
    query = """INSERT INTO coordinates VALUES(?, ?, ?)"""
    try:
        cursor = conn.cursor()
        cursor.execute(query, (id, coordinate[0], coordinate[1]))
        conn.commit()

    except sqlite3.Error as e:
        print(e)


numberOfDb = int(input("The number of databases: "))
path = input("Path for the databases: ")
frequency = int(input("Frequency (1/s): "))
low = int(input("The lowest boundary: "))
high = int(input("The highest boundary: "))

dbs = list()
for i in range(numberOfDb):
    name = "db_" + str(i) + ".db"
    pathOfDb = path + "/databases/" + name

    conn = create_connection(pathOfDb)
    create_coordinate_table(conn)
    conn.close()

    dbs.append(pathOfDb)


startTime = time.time()
id = 1
while True:
    for i in range(numberOfDb):
        conn = create_connection(dbs[i])

        coordinate = coordinate_generator(low, high)
        insert_coordinate(conn, id, coordinate)
        conn.close()

        print("coordinate:", coordinate)
        print("path:", dbs[i])
        print("--------------------------")

    id += 1
    time.sleep(1 / frequency)
