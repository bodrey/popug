from django.core.management.base import BaseCommand
from django.utils import autoreload
# from service.models import *
from service.views import *
import pika
import sys
import json
from jsonschema import validate
from asyncs import *

def check_auth(data):
    try:
        user = User.objects.filter(token = data['token']).first()
        if user:
            return user.user_id
        else:
            return None
    except:
        return None
    
class Command(BaseCommand):
    help = 'Runs rabbit listener'

    def callback(self, ch, method, properties, body):
        self.stderr.write(f'RabbitConsuming: callback {str(json.loads(body))}')
        # self.stderr.write(f'callback {str(properties)}')
        # self.stderr.write(str(body))

        data = json.loads(body)

        try:
            validate(instance=data, schema=schema_task_to_auth)
            meow('schema_task_to_auth is good')
            ch.basic_publish(exchange='',
                routing_key=properties.reply_to,
                body=json.dumps({'user_id': check_auth(data)})
            )
        except:
            meow(schema_task_to_auth)
            meow(data)
            meow('schema_task_to_auth is NOT')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    @staticmethod
    def _get_connection():
        credentials = pika.PlainCredentials('user', 'password')
        return pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))

    def handle(self, *args, **kwargs):
        # autoreload.run_with_reloader(self)
        self.stderr.write("RabbitConsuming: start")
        connection = self._get_connection()
        channel = connection.channel()

        channel.queue_declare(queue='check_auth')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume('check_auth', self.callback)

        channel.start_consuming()

 
