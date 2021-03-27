# Generated by Django 3.1 on 2021-02-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20201221_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitaciones',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='identificación',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='teléfono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='habitaciones',
            name='nro_habitacion',
            field=models.IntegerField(),
        ),
    ]