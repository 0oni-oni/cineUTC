# Generated by Django 4.0.6 on 2024-06-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0008_genero_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='fotografia',
            field=models.FileField(blank=True, null=True, upload_to='portadas'),
        ),
    ]
