# Generated by Django 3.2 on 2022-11-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20221016_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='pictures/thumb/'),
        ),
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='pictures/thumb/'),
        ),
        migrations.AlterField(
            model_name='information',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]