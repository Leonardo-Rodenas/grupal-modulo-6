# Generated by Django 4.2.1 on 2023-06-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telovendoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('rep_legal', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=10)),
                ('dirección', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
