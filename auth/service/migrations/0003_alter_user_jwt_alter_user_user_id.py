# Generated by Django 5.0 on 2024-03-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='jwt',
            field=models.TextField(blank=True, verbose_name='JWT-Токен'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, max_length=200, verbose_name='Попуг id'),
        ),
    ]
