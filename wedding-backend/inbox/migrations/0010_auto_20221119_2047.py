# Generated by Django 3.2 on 2022-11-19 20:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inbox', '0009_response_active'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='response',
            name='unique_user_response',
        ),
        migrations.AddField(
            model_name='response',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='response',
            unique_together={('question', 'user', 'active', 'deleted_at')},
        ),
    ]
