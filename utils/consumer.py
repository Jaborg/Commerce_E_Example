from confluent_kafka import Consumer, KafkaError
import json

import utils.database_functions as dbf
from utils.constants import kafka_consume_conf,postgres_config


def consume_from_kafka():
    
    consumer = Consumer(kafka_consume_conf)
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
            dbf.store_data_in_db(postgres_config,event_data)
            print(event_data)
        
