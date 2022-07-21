# Generated by Django 3.2.14 on 2022-07-20 02:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 7, 20, 2, 26, 39, 473394, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 7, 20, 2, 26, 43, 175690, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
