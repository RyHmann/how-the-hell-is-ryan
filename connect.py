import psycopg2
from config import psql_config


def connect_to_psql():
    connection = None
    try:
        params = psql_config()
        print('Connecting to psql db...')
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        print("PostgreSQL database version:")
        cursor.execute('SELECT version()')

        db_version = cursor.fetchone()
        print(db_version)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    connect_to_psql()