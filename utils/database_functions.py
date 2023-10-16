import psycopg2-binary



config = {'host':"localhost",          # Change if your DB is on another machine
    'database':"ConsumeDB",
    'user':"Jaborg1258",
    'password':"Sains1258"}


def sql_connect(config):

    connection = psycopg2.connect(
    host=config['host'],   
    database=config['database'],
    user=config['user'],
    password=config['password']
)
    cursor = connection.cursor()

    return cursor


def sql_execute(sql,type)

    cursor = sql_connect(config)
    if type == 'insert':
        cursor.execute(sql.read_file('.sql_scripts/insert_main.sql'),sql)


    return