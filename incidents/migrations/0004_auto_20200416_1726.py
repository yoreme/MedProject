# Generated by Django 3.0.5 on 2020-04-16 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0003_auto_20200416_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='type',
            new_name='incident_type',
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 17, 25, 44, 928114)),
        ),
    ]
