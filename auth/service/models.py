from django.db import models

class User(models.Model):
    name = models.CharField('Имя', max_length=200)
    password = models.CharField('Пароль', max_length=200)
    token = models.TextField('JWT-Токен', blank=True)
    email = models.EmailField(verbose_name="E-mail", blank=True)
    ROLE_CHOICES = [
        ('admin','Админ'),
        ('chief','Начальник'),
        ('popug', 'Разработчик'),
        ('manager', 'Менеджер'),
        ('accountant', 'Бухгалтер'),
    ]
    role = models.CharField('Статус', max_length=20, choices = ROLE_CHOICES, default='popug')
    # user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField('Попуг id', max_length=200, blank=True)
