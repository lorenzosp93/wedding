# Generated by Django 3.2 on 2022-11-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_alter_userprofile_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.IntegerField(choices=[(2, 'family'), (3, 'friend'), (5, 'colleague')], default=2),
        ),
    ]
