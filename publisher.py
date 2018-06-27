import pika
import sys

with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    message = ' '.join(sys.argv[1:]) or 'info: hello world'

    channel.basic_publish(
        exchange="logs",
        routing_key="",
        body=message
    )

    print("[*] Sent message : {}".format(message))
