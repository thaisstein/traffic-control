#!/usr/bin/env python
import pika
from pika.exchange_type import ExchangeType
import sys
import time

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = "Welcome to Traffic Information"

channel.basic_publish(exchange='pubsub', routing_key='', body=message)
print("sent message: {message}")
connection.close