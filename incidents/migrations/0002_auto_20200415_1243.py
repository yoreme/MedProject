# Generated by Django 3.0.5 on 2020-04-15 11:43

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='incident_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 12, 43, 10, 196139)),
        ),
        migrations.AddField(
            model_name='incident',
            name='reference_number',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='type',
            field=models.CharField(blank=True, choices=[('Risk', 'Risk'), ('Near miss', 'Near miss'), ('Near miss', 'Adverse Event')], default='Risk', max_length=10, null=True),
        ),
    ]
