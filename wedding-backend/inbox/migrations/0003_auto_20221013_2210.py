# Generated by Django 3.2 on 2022-10-13 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_auto_20221013_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='type',
        ),
        migrations.RemoveField(
            model_name='question',
            name='type',
        ),
        migrations.AddField(
            model_name='question',
            name='free_text',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='multi_select',
            field=models.BooleanField(default=False),
        ),
    ]
