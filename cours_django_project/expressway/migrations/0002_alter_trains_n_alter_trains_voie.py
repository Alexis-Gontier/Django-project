# Generated by Django 5.0.3 on 2024-03-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expressway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='n',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trains',
            name='voie',
            field=models.IntegerField(),
        ),
    ]