# Generated by Django 3.1 on 2021-02-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0014_auto_20210225_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='fecha_entrada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='fecha_salida',
            field=models.DateField(),
        ),
    ]
