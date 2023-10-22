
kafka_produce_conf = {
    'bootstrap.servers': 'kafka:9092',  
    'client.id': 'python-producer'
}

kafka_consume_conf = {
    'bootstrap.servers': 'kafka:9092',  # e.g. 'localhost:9092' or 'kafka:9093'
    'group.id': 'sales_group',
    'auto.offset.reset': 'earliest'
}

postgres_config = {
    'host': "postgres",
    'port': 5432,
    'database': "ConsumeDB",
    'user': "Jaborg1258",
    'password': "Sains1258"
}