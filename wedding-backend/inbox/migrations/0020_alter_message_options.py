# Generated by Django 4.1.6 on 2023-07-04 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0019_alter_message_audience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['created_at']},
        ),
    ]
