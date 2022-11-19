# Generated by Django 3.2 on 2022-11-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0007_message_audience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='audience',
            field=models.IntegerField(choices=[(2, 'family'), (3, 'friend'), (5, 'colleague'), (6, 'family & friend'), (10, 'family & colleague'), (15, 'friend & colleague'), (30, 'all')], default=30),
        ),
    ]