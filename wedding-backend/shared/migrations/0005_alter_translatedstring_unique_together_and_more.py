# Generated by Django 4.1.3 on 2023-01-25 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0004_delete_attachment_remove_location_address_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='translatedstring',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='translatedstring',
            constraint=models.UniqueConstraint(fields=('language', 'content'), name='unique_translation_per_language_and_content'),
        ),
    ]