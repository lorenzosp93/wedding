# Generated by Django 4.1.3 on 2022-12-24 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_alter_translatedstring_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attachment',
        ),
        migrations.RemoveField(
            model_name='location',
            name='address',
        ),
        migrations.DeleteModel(
            name='SiteSetting',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]