# Generated by Django 2.1.2 on 2018-10-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0003_user_is_moderator'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
