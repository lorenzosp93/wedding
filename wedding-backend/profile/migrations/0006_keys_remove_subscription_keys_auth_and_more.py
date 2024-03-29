# Generated by Django 4.1.3 on 2022-11-30 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p265dh', models.CharField(max_length=100)),
                ('auth', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='keys_auth',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='keys_p265dh',
        ),
        migrations.AddField(
            model_name='subscription',
            name='keys',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profile.keys', unique=True),
            preserve_default=False,
        ),
    ]
