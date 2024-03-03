# Generated by Django 5.0 on 2024-03-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('password', models.CharField(max_length=200, verbose_name='Имя')),
                ('jwt', models.TextField(verbose_name='JWT-Токен')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('role', models.CharField(choices=[('admin', 'Админ'), ('chief', 'Начальник'), ('popug', 'Разработчик'), ('manager', 'Менеджер'), ('accountant', 'Бухгалтер')], default='popug', max_length=20, verbose_name='Статус')),
                ('user_id', models.CharField(max_length=200, verbose_name='Попуг id')),
            ],
        ),
    ]