# Generated by Django 2.1.2 on 2018-11-21 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0016_alert'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='been_sent',
            new_name='has_been_sent',
        ),
    ]
