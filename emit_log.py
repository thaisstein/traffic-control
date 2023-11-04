#!/usr/bin/env python
import pika
from pika.exchange_type import ExchangeType
import sys, asyncio, websockets
import random
import time
import pandas as pd  # Import the pandas library for reading CSV files



rabbitmq_host = 'localhost'
exchange_name = 'pubsub'

while True:
    # Check your variable in real-time
    # Read the traffic.csv file
    try:
        df = pd.read_csv('traffic.csv')
        # Assuming there is a column named 'number_of_vehicles'
        number_of_vehicles = df['Vehicles'].values[0]

        my_variable = random.randint(0, 6)

        if number_of_vehicles > 20:
            message = "*** Attention! Big number of vehicles on the route ***"
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
            channel = connection.channel()
            channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')
            channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
            print(f"Sent: {message}")
            connection.close()
            
        if my_variable == 1:
            message = "*** Attention! Busy traffic on route close to you! ***"
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
            channel = connection.channel()
            channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')
            channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
            print(f"Sent: {message}")
            connection.close()

        if my_variable == 4:
            message = "*** Careful! Accident close to you! ***"
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
            channel = connection.channel()
            channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')
            channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
            print(f"Sent: {message}")
            connection.close()

    except Exception as e:
        # Handle exceptions, such as file not found or CSV format errors
        print(f"Error reading traffic.csv: {str(e)}")

    time.sleep(1)  


