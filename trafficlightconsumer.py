import pika
import time
from trafficlightsimulation import countdown_timer, draw_traffic_light

def on_message_received(ch, method, properties, body):
    global countdown_time  # Use the global variable
    print("Received alert")
    countdown_time = 3
    draw_traffic_light('Green')
    countdown_timer('Green', countdown_time)
    draw_traffic_light('Red')
    countdown_timer('Red', countdown_time)

def start_rabbitmq_consumer():
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.exchange_declare(exchange='pubsub', exchange_type='fanout')
    queue = channel.queue_declare(queue='', exclusive=True)
    channel.queue_bind(exchange='pubsub', queue=queue.method.queue)
    channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)
    print("Starting Consuming")
    channel.start_consuming()

if __name__ == "__main__":
    countdown_time = 5
    start_rabbitmq_consumer()
