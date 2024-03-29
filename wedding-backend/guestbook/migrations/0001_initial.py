# Generated by Django 4.1.3 on 2022-12-29 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last modified date')),
                ('active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('text', models.TextField(max_length=280)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
