# Generated by Django 4.1.6 on 2023-07-04 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0021_alter_question_options_question_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='modified_at',
        ),
    ]
