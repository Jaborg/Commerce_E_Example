from confluent_kafka import Producer
import json


from produce_utils import Sales_Event,delivery_report



if __name__ == "__main__": 
    conf = {
    'bootstrap.servers': 'localhost:9092',  # Assuming your Kafka broker is running locally
    'client.id': 'python-producer'
}
    producer = Producer(conf)



    for _ in range(100):  # Produce 100 sales events
        event = Sales_Event()
        serialized_event = json.dumps(vars(event))
        producer.produce('sales', key=str(event.product_id), value=serialized_event, callback=delivery_report)

        # Wait for any outstanding messages to be delivered and delivery reports to be received.
        producer.poll(0)
    producer.flush()