import pandas as pd
import sqlite3


def create_db():
    df = pd.read_csv('./data/btcusd_1-min_data.csv')


    #create table
    connection = sqlite3.connect('btc_data.db')

    cursor = connection.cursor()

    cmd1 = """CREATE TABLE IF NOT EXISTS
    btc_data(timestamp FLOAT PRIMARY KEY, open FLOAT, high FLOAT, low FLOAT, close FLOAT, volume FLOAT)"""

    cursor.execute(cmd1)
    
    #transfer csv data to to the db

    data_rows = df.values.tolist()

    data_to_add = [(row[0], row[1], row[2], row[3], row[4], row[5]) for row in data_rows]

    cursor.executemany("INSERT INTO btc_data VALUES(?, ?, ?, ?, ?, ?)", data_to_add)

    connection.commit()
    connection.close()

create_db()