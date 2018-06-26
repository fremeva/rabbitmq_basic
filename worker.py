import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="importers")


def importers(ch, method, properties, body):
    time.sleep(5)
    print(body)
    #  Para cuando deseamos enviar la respuesta al publisher
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(importers, queue="importers", no_ack=False)

print('Inicio del Worker')

channel.start_consuming()
