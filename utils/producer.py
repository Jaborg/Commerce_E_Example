from confluent_kafka import Producer
import json
import random
import time
from datetime import datetime


conf = {
    'bootstrap.servers': 'kafka:9092',  
    'client.id': 'python-producer'
}

class Sales_Event:

    def __init__(self):
        products = ['laptop', 'mouse', 'monitor', 'keyboard', 'headset']
        self.product_id =product_id = random.choice(range(1, 6))
        self.product_name = products[product_id - 1]
        self.quantity = random.choice(range(1, 11))
        self.price = random.choice(range(10, 151))  # Random price between 10 and 150
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))




def produce_to_kafka():


    producer = Producer(conf)



    for _ in range(100):  # Produce 100 sales events
        event = Sales_Event()
        serialized_event = json.dumps(vars(event))
        producer.produce('sales', key=str(event.product_id), value=serialized_event, callback=delivery_report)

        # Wait for any outstanding messages to be delivered and delivery reports to be received.
        producer.poll(0)
    producer.flush()