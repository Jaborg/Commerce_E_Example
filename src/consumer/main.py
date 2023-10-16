from confluent_kafka import Consumer, KafkaError
import json

from consume_utils import store_data_in_db,process_message,conf


if __name__ == "__main__": 

    
    consumer = Consumer(conf)
    consumer.subscribe(['sales'])

    while True:
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
            store_data_in_db(event_data)
            print(event_data)
            


            
            # Store processed data
            # store_data_in_db(product_id, total_sales)
