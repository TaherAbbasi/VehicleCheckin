# Generated by Django 3.1.6 on 2021-02-16 22:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_api', '0004_auto_20210216_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='vehicle',
            field=models.ForeignKey(default=datetime.datetime(2021, 2, 16, 15, 14, 11, 101044), on_delete=django.db.models.deletion.PROTECT, to='checkin_api.vehicle'),
        ),
    ]
