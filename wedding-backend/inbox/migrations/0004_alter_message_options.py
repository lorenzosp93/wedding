# Generated by Django 3.2 on 2022-10-16 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0003_auto_20221013_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_at']},
        ),
    ]