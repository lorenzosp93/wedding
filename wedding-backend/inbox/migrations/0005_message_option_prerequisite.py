# Generated by Django 3.2 on 2022-11-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0004_alter_message_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='option_prerequisite',
            field=models.ManyToManyField(blank=True, to='inbox.Option'),
        ),
    ]
