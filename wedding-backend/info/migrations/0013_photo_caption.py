# Generated by Django 4.1.3 on 2022-12-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_alter_informationwidget_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]