import psycopg2

from utils.common_functions import read_file


def sql_connect(config):
    try:
        connection = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )
        cursor = connection.cursor()
        return connection, cursor
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None, None


def sql_execute(config, sql, query_type):
    connection, cursor = sql_connect(config)
    if not connection or not cursor:
        return

    try:
        if query_type == 'insert':
            sql_command = read_file('./sql_scripts/insert_main.sql')
            cursor.execute(sql_command, sql)
            connection.commit()
        # Add more query types as needed
    except Exception as e:
        print(f"Error executing SQL: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def store_data_in_db(config, data):
    sql_execute(config, data, 'insert')
