# Generated by Django 2.1.2 on 2018-10-18 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0004_artist_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
