# Generated by Django 3.0.5 on 2020-04-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0005_auto_20200419_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='incident_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
