# Generated by Django 3.0.5 on 2020-04-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0006_auto_20200422_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='incident_date',
            field=models.DateTimeField(),
        ),
    ]
