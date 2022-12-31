# Generated by Django 4.1.3 on 2022-12-29 13:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_alter_entry_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='id',
        ),
        migrations.AddField(
            model_name='entry',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]