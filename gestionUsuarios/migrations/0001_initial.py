# Generated by Django 3.0.2 on 2020-11-12 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('contra', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tfno', models.CharField(max_length=10)),
            ],
        ),
    ]
