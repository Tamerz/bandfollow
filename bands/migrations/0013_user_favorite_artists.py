# Generated by Django 2.1.2 on 2018-11-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0012_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_artists',
            field=models.ManyToManyField(to='bands.Artist'),
        ),
    ]