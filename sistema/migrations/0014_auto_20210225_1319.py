# Generated by Django 3.1 on 2021-02-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0013_auto_20210225_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='fecha_entrada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='fecha_salida',
            field=models.DateTimeField(),
        ),
    ]
