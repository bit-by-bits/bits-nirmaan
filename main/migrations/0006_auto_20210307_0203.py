# Generated by Django 2.2 on 2021-03-06 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210108_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 20, 33, 12, 726633, tzinfo=utc)),
        ),
    ]
