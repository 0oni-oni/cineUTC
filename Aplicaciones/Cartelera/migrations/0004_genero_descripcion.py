# Generated by Django 4.0.6 on 2024-05-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0003_rename_apellidoy7_director_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='Descripcion',
            field=models.CharField(default='', max_length=150),
        ),
    ]
