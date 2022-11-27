# Generated by Django 4.1.3 on 2022-11-25 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_alter_translatedstring_language'),
        ('info', '0006_information_audience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['type']},
        ),
        migrations.AlterField(
            model_name='information',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_subject', to='shared.contentstring'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='type',
            field=models.IntegerField(choices=[(0, 'Before'), (1, 'Ice-breaker'), (2, 'Ceremony'), (3, 'Reception'), (4, 'Dinner'), (5, 'Dance')]),
        ),
    ]