# Generated by Django 3.2 on 2022-11-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0006_rename_option_prerequisite_message_option_pre'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='audience',
            field=models.IntegerField(choices=[(2, 'family'), (3, 'friend'), (5, 'colleague'), (6, 'family & friend'), (10, 'family & colleague'), (15, 'friend & colleague'), (30, 'all')], default=4),
        ),
    ]
