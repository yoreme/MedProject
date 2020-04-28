# Generated by Django 3.0.5 on 2020-04-28 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lookups', '0002_auto_20200426_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='third_category',
            name='first_category',
        ),
        migrations.AddField(
            model_name='third_category',
            name='firstcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstcategory', to='lookups.First_Category'),
        ),
        migrations.AlterField(
            model_name='third_category',
            name='secondcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondcategory', to='lookups.Second_Category'),
        ),
    ]
