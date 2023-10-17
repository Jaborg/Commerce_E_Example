from confluent_kafka import Consumer, KafkaError
import json

import utils.database_functions as dbf

conf = {
    'bootstrap.servers': 'kafka:9092',  # e.g. 'localhost:9092' or 'kafka:9093'
    'group.id': 'sales_group',
    'auto.offset.reset': 'earliest'
}





# def store_data_in_db(data):

#     dbf.sql_execute(data,'insert')
    
#     pass



def consume_from_kafka():
    
    consumer = Consumer(conf)
    consumer.subscribe(['sales'])

    for x in range(100):
        msg = consumer.poll(1.0)

        if msg is None:
            print('None')
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Reached end of topic')
            else:
                print('Error while consuming message: {}'.format(msg.error()))
        else:

            event_data = json.loads(msg.value().decode('utf-8').replace("'", "\""))
            # store_data_in_db(event_data)
            print(event_data)
        
