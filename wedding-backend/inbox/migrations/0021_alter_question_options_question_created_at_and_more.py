# Generated by Django 4.1.6 on 2023-07-04 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0020_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Last modified date'),
        ),
    ]
