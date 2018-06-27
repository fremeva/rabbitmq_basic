import pika

with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    results = channel.queue_declare(exclusive=True)
    queue_name = results.method.queue
    channel.queue_bind(exchange='logs', queue=queue_name)

    print('[*] Starting worker with queue {}'.format(queue_name))


    def callback(ch, method, properties, body):
        print('[*] Message for broker {} : {}'.format(queue_name, body))


    channel.basic_consume(callback, queue=queue_name, no_ack=True)
    channel.start_consuming()
