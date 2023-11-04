# Traffic Control System

This is a distributed system project made for the final Middleware project, a couse offered by the Computer Science For Networks course at l'Institut Polytéchnique de Paris.
In this system the RabbitMQ message broker and the FastAPI library are used to create an integrated pub/sub system. 

## Description

This project aims to create a real-time traffic monitoring system that uses cameras to detect accidents and traffic jams.
The system then sends immediate alerts to subscribers, including drivers, traffic lights, and emergency services, enabling quicker responses and reducing social costs associated with road incidents.

## Key Components

- **Camera-based Detection**: Utilizing cameras for real-time monitoring of road conditions.
- **Alert Distribution**: Sending instant alerts to subscribed users and traffic infrastructure.
- **Improved Response Time**: Enhancing response times to accidents and traffic issues, leading to reduced societal costs.

## Architecture Overview

![Screen Shot 2023-11-04 at 3 19 35 PM](https://github.com/thaisstein/traffic-control/assets/52481495/3b97682f-8da0-4721-a6af-bf903c0141fe)

## Installation

1. Clone or download the repository.
2. Ensure you have RabbitMQ running on Docker. I used the managment image with the following command:

```bash
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```
3. To run the producer and the subscriber:
```bash
python emit_log.py
```
```bash
python firstconsumer.py
```
4. To run the web server:
```bash
python main.py
```
## Traffic Lights Integration
I developed a system to program traffic lights more effectively by training a neural network with **scikit-learn. **
This system relies on five CSV databases, including real-time traffic data and four additional databases generated using the neural network, which provide predictions for traffic conditions over the next four months.
![Screen Shot 2023-11-04 at 3 36 10 PM](https://github.com/thaisstein/traffic-control/assets/52481495/77ea75e8-dfde-49f4-b0aa-637c1ad51861)

## Future Enhancements

- **Scalability and Robustness**: Exploring methods to scale the system to handle larger volumes of data and traffic while ensuring its robustness and reliability.

- **Message Brokers**: Further research and development of message brokers to enhance message handling and distribution efficiency.

- **Machine Learning Improvements**: Continuously refining machine learning models to improve the accuracy of traffic predictions and adapt to changing conditions.

- **Real-time Data Sources**: Integrating additional real-time data sources to enhance the accuracy and timeliness of traffic information.
