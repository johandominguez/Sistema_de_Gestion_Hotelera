# Generated by Django 3.1 on 2021-02-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0009_auto_20210222_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
