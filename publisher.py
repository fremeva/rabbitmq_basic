import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue="importers")
channel.basic_publish(
    exchange="",
    routing_key="importers",
    body="Hola a todos! 3"
)
print("Finalizado")

connection.close()
