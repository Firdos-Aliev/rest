# Generated by Django 3.2.3 on 2021-05-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Время добавления/обновления'),
        ),
    ]
