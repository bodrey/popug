# Generated by Django 4.2.10 on 2024-03-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assign_value',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Цена назначения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='done_value',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Цена выполнения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user_id',
            field=models.CharField(blank=True, max_length=200, verbose_name='Попуг id'),
        ),
    ]
