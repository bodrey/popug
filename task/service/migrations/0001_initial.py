# Generated by Django 4.2.10 on 2024-03-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('status', models.CharField(choices=[('assigned', 'Назначено'), ('done', 'Выполнено')], default='assigned', max_length=20, verbose_name='Статус')),
                ('description', models.TextField(verbose_name='Описание')),
                ('assign_value', models.PositiveSmallIntegerField(verbose_name='Цена назначения')),
                ('done_value', models.PositiveSmallIntegerField(verbose_name='Цена выполнения')),
                ('user_id', models.CharField(max_length=200, verbose_name='Попуг id')),
            ],
        ),
    ]
