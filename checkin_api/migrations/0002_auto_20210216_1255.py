# Generated by Django 3.1.6 on 2021-02-16 19:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='in_datetime',
            new_name='log_datetime',
        ),
        migrations.RemoveField(
            model_name='log',
            name='out_datetime',
        ),
        migrations.AddField(
            model_name='log',
            name='enter',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='vehicle',
            field=models.ForeignKey(default=datetime.datetime(2021, 2, 16, 12, 55, 11, 718470), on_delete=django.db.models.deletion.PROTECT, to='checkin_api.vehicle'),
        ),
    ]
