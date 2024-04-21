import sqlite3
import queries as q
import pandas as pd

# DB Connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    # step 2- Make the cursor
    curs = conn.cursor()
    # Execute the query
    curs.execute(query)
    # pull and return
    return curs.fetchall()


if __name__=="__main__":
    conn = connect_to_db()
    # print(execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)

    # change the tuples to dataframes
    df = pd.DataFrame(results)
    # Lets name the columns
    df.columns = ['name', 'average_item_weight']
    # turn the dataframe and save it to csv file
    df.to_csv('rpg_db.csv', index=False)
    print(df.head())