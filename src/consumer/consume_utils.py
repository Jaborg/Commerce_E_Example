import utils.database_functions 

conf = {
    'bootstrap.servers': 'kafka:9092',  # e.g. 'localhost:9092' or 'kafka:9093'
    'group.id': 'sales_group',
    'auto.offset.reset': 'earliest'
}

#{'product_id': 2, 'product_name': 'mouse', 'quantity': 10, 'price': 31, 'timestamp': '2023-10-11 19:14:05'}


def store_data_in_db(data):

    utils.database_functions.sql_execute(data,'insert')
    
    pass

