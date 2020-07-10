# Generated by Django 2.0 on 2020-07-10 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0021_auto_20200710_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='date_started',
            field=models.DateField(default=datetime.datetime(2020, 7, 10, 12, 58, 5, 743201, tzinfo=utc), verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='initiativecomment',
            name='published_on',
            field=models.DateField(default=datetime.datetime(2020, 7, 10, 12, 58, 5, 770696, tzinfo=utc)),
        ),
    ]
