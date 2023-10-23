import pika
import websockets
import asyncio
import threading

async def send_messages_to_websocket(messages):
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        for message in messages:
            await websocket.send(message)


def on_message_received(ch, method, properties, body):
    message = body.decode("utf-8")
    # Process the message as needed
    print(f"Received message: {message}")
    messages_to_send = [message]  # You can collect multiple messages if needed
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_messages_to_websocket(messages_to_send))


def start_consumer():
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.exchange_declare(exchange='pubsub', exchange_type='fanout')
    queue = channel.queue_declare(queue='', exclusive=True)
    channel.queue_bind(exchange='pubsub', queue=queue.method.queue)
    channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

    print("Starting Consuming")

    # Start the consuming process (in a new thread)
    channel.start_consuming()

if __name__ == "__main__":
    # Create a new thread to run the WebSocket consumer
    websocket_thread = threading.Thread(target=start_consumer)
    websocket_thread.start()