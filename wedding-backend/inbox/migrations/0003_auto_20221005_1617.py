# Generated by Django 3.2 on 2022-10-05 16:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_auto_20221005_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='usermessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermessage',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Last modified date'),
        ),
    ]
