# Generated by Django 4.1.3 on 2022-12-12 16:37

from django.db import migrations, models
import django.db.models.deletion
import info.models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_informationwidget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationwidget',
            name='content',
            field=models.TextField(validators=[]),
        ),
        migrations.AlterField(
            model_name='informationwidget',
            name='info',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='widget', to='info.information'),
        ),
    ]
