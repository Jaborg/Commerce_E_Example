
conf = {
    'bootstrap.servers': 'localhost:9092',  # e.g. 'localhost:9092' or 'kafka:9093'
    'group.id': 'sales_group',
    'auto.offset.reset': 'earliest'
}


def process_message(msg_value):
    # Extract data from your message. This assumes a simple string; adjust if your message is JSON, etc.
    data = msg_value.split(',')
    product_id, quantity, price = data[0], data[1], data[2]
    # Calculate total sales amount
    total_sales = int(quantity) * float(price)
    
    # Return processed data
    return product_id, total_sales

def store_data_in_db(product_id, total_sales):
    # Connect to your database (e.g., PostgreSQL) and store the data. 
    # This is just a placeholder function; you'll need to implement database connection and insertion logic.
    pass
