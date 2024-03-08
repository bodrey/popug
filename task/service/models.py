from django.db import models

class Task(models.Model):
    name = models.CharField('Название', max_length=200)
    STATUS_CHOICES = [
        ('assigned', 'Назначено'),
        ('done','Выполнено'),
    ]
    status = models.CharField('Статус', max_length=20, choices = STATUS_CHOICES, default='assigned')
    description = models.TextField('Описание', blank=True)
    #  value = models.PositiveSmallIntegerField(verbose_name="Цена", validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    assign_value = models.PositiveSmallIntegerField('Цена назначения', blank=True, null = True)
    done_value = models.PositiveSmallIntegerField('Цена выполнения', blank=True, null = True)
    # user_uuid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Попуг")
    # user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField('Попуг id', max_length=200, blank=True)

# class User