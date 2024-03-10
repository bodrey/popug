# import threading
# import pika
# from django.conf import settings

# class RabbitConsuming(threading.Thread):
#     def callback(self, ch, method, properties, body):
#         print("RabbitConsuming: callback")
#         print(ch, method, properties, body)
#         # do something
#         pass

#     @staticmethod
#     def _get_connection():
#         credentials = pika.PlainCredentials('user', 'password')
#         return pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))

#     def run(self):
#         print("RabbitConsuming: start")
#         connection = self._get_connection()
#         channel = connection.channel()

#         channel.queue_declare(queue='check_auth')

#         channel.basic_qos(prefetch_count=1)
#         channel.basic_consume('check_auth', self.callback)

#         channel.start_consuming()
