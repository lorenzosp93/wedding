# Generated by Django 4.1.3 on 2022-11-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_alter_photo_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='submit',
            field=models.BooleanField(default=False),
        ),
    ]
