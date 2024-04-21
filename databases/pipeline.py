import psycopg2
from queries import GET_CHARACTERS
from sqlite_connection import connect_to_db, execute_q

# Postgress connection Credetials

# User and default database from ELEphant sql
DBNAME = 'pjksxssb'
USER = 'pjksxssb'
# pssword from elephant sql
PASSWORD = 'wK01rRzqfi2AHOcB0wHEQRlzwCK4sj0X'
# server from elephant sql
HOST = 'jelani.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname =DBNAME, user=USER, password = PASSWORD, host = HOST)
pg_curs = pg_conn.cursor()


if __name__=="__main__":
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)
    print(sl_characters[:5])
    # pg_curs.execute(INSERT_TEST_TABLE)
    # pg_conn.commit()

