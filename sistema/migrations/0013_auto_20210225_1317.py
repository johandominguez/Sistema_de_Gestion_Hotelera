# Generated by Django 3.1 on 2021-02-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0012_auto_20210225_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='cant_adultos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='cant_niños',
            field=models.IntegerField(null=True),
        ),
    ]
