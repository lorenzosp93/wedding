# Generated by Django 5.0 on 2024-01-14 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0005_alter_translatedstring_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ByteArray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.BinaryField()),
            ],
        ),
    ]