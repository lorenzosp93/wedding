# Generated by Django 3.2 on 2022-07-04 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared', '0002_alter_attachment_id_alter_authorable_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.TextField(blank=True, null=True)),
                ('address2', models.TextField(blank=True, null=True)),
                ('city', models.TextField()),
                ('postal_code', models.TextField()),
                ('province_or_state', models.TextField(blank=True, null=True)),
                ('country', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.IntegerField(choices=[(0, 'en'), (1, 'it'), (2, 'es')])),
                ('type', models.IntegerField(choices=[(0, 'family'), (1, 'friend'), (2, 'colleague')])),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shared.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=15, max_digits=17, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=15, max_digits=17, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shared.address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
