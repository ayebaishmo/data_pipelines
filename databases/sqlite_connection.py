import sqlite3
import queries as qu
import pandas as pd
def connect_to_db(db_name = 'rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, qu.GET_CHARACTERS)
    # print(results[::5])

    # change the tuples to dataframes
    df = pd.DataFrame(results)
    print(df.head())