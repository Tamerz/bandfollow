# Generated by Django 2.1.2 on 2018-11-21 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0015_auto_20181121_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('been_sent', models.BooleanField(default=False)),
                ('event', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='bands.Event')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]