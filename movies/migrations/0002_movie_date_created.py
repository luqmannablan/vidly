# Generated by Django 2.1 on 2024-02-03 22:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 22, 19, 52, 270161, tzinfo=utc)),
        ),
    ]