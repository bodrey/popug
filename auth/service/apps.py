from django.apps import AppConfig
from service.util import *

class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'
    # def ready(self):
    #     print("ready", self)
    #     consumer = RabbitConsuming()
    #     consumer.daemon = True
    #     consumer.setDaemon(True)
    #     consumer.start()
    #     print("started3", consumer)
