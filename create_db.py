import pandas as pd
import sqlite3


def create_db(df):

    #create table
    connection = sqlite3.connect('./data/btc_data.db')

    cursor = connection.cursor()

    cmd1 = """CREATE TABLE IF NOT EXISTS
    btc_data(Timestamp FLOAT PRIMARY KEY, Open FLOAT, 
    High FLOAT, Low FLOAT, Close FLOAT, Volume FLOAT, Datetime TEXT)"""

    cursor.execute(cmd1)
    
    #create the datetimes values entry
    df['Datetime'] = pd.to_datetime(df['Timestamp'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')

    #transfer csv data to to the db
    data_rows = df.values.tolist()    


    data_to_add = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in data_rows]

    cursor.executemany("INSERT or REPLACE INTO btc_data VALUES(?, ?, ?, ?, ?, ?, ?)", data_to_add)

    connection.commit()
    connection.close()



df = pd.read_csv('./data/btcusd_1-min_data.csv')
#clean_data(df)
create_db(df)

