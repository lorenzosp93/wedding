# Generated by Django 3.2 on 2022-11-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0008_alter_message_audience'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]