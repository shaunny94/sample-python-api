import psycopg2

def connect():
    try:
        conn = psycopg2.connect("dbname=postgres user=postgres password=admin")
        return conn
    except:
        print('Unable to connect to postgres')

def close(connection):
    if(connection):
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")