# Generated by Django 4.1.3 on 2022-11-25 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_alter_translatedstring_language'),
        ('inbox', '0010_auto_20221119_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_subject', to='shared.contentstring'),
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_subject', to='shared.contentstring'),
        ),
    ]