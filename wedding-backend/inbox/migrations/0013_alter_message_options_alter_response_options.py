# Generated by Django 4.1.3 on 2022-12-29 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0012_message_submit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['-pk']},
        ),
    ]