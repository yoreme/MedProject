# Generated by Django 3.0.5 on 2020-04-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('place', models.CharField(max_length=50)),
                ('personal_number', models.CharField(max_length=12)),
                ('description', models.TextField(max_length=500)),
                ('action', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('ip_address', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=40)),
                ('longitude', models.CharField(max_length=40)),
                ('country_name', models.CharField(max_length=20)),
                ('country_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
