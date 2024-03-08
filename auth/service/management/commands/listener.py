from django.core.management.base import BaseCommand
import pika

class Command(BaseCommand):
    help = 'Runs rabbit listener'

    def callback(self, ch, method, properties, body):
        self.stderr.write(f'RabbitConsuming: callback {str(body)}')
        self.stderr.write(f'callback {str(properties)}')
        # self.stderr.write(body)
        # do something
        ch.basic_publish(exchange='',
                        routing_key=properties.reply_to,
                        # properties=pika.BasicProperties(correlation_id = \
                        #                                     properties.correlation_id),
                        body=str("userOK"))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        pass

    @staticmethod
    def _get_connection():
        credentials = pika.PlainCredentials('user', 'password')
        return pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))

    def handle(self, *args, **kwargs):
        self.stderr.write("RabbitConsuming: start")
        connection = self._get_connection()
        channel = connection.channel()

        channel.queue_declare(queue='check_auth')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume('check_auth', self.callback)

        channel.start_consuming()
