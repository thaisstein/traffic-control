#!/usr/bin/env python
import pika
from pika.exchange_type import ExchangeType
import sys, asyncio, websockets
import random
import time

rabbitmq_host = 'localhost'
exchange_name = 'pubsub'

while True:
    # Check your variable in real-time
    my_variable = random.randint(0, 5)

    if my_variable == 1:
        message = "Attention! Busy traffic on route close to you!"
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')
        channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
        print(f"Sent: {message}")
        connection.close()

    if my_variable == 4:
        message = "Careful! Accident close to you!"
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')
        channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
        print(f"Sent: {message}")
        connection.close()

    # Adjust the checking interval
    time.sleep(1)  


