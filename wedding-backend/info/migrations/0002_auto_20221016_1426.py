# Generated by Django 3.2 on 2022-10-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='name',
        ),
        migrations.RemoveField(
            model_name='information',
            name='slug',
        ),
        migrations.AlterField(
            model_name='information',
            name='type',
            field=models.IntegerField(choices=[(0, 'Venues'), (1, 'Food'), (2, 'Attractions'), (3, 'Tips'), (4, 'Travel'), (5, 'Events')]),
        ),
    ]
