from fastapi import FastAPI, WebSocket
import pika
import asyncio

app = FastAPI()

# WebSocket connection management as per your existing code
connected_websockets = []

def send_update_to_clients(message):
    for websocket in connected_websockets:
        websocket.send_text(message)

def rabbitmq_callback(ch, method, properties, body):
    message = body.decode()
    send_update_to_clients(message)

def start_rabbitmq_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='logs', queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=rabbitmq_callback, auto_ack=True)
    channel.start_consuming()

async def send_periodic_haha_messages():
    while True:
        await asyncio.sleep(5)  # Send a message every 5 seconds
        message = "HAHA"
        send_update_to_clients(message)

