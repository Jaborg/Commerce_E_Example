import random
import time
from datetime import datetime

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