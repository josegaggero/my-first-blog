# Generated by Django 2.2.16 on 2020-10-20 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetasapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.TextField(max_length=30)),
                ('clave', models.TextField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.TextField(max_length=25),
        ),
    ]