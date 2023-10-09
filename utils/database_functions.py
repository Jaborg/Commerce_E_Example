import psycopg2

connection = psycopg2.connect(
    host="localhost",          # Change if your DB is on another machine
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
cursor = connection.cursor()

# Execute SQL queries using cursor as needed.

cursor.close()
connection.close()

config = {'host':"localhost",          # Change if your DB is on another machine
    'database':"mydatabase",
    'user':"myuser",
    'password':"mypassword"}


def sql_connect(config):

    connection = psycopg2.connect(
    host=config['host'],   
    database=config['database'],
    user=config['user'],
    password=config['password']
)
    cursor = connection.cursor()


de