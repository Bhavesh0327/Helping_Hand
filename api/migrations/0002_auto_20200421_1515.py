# Generated by Django 3.0.5 on 2020-04-21 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='district_id',
        ),
        migrations.RemoveField(
            model_name='request',
            name='service_id',
        ),
    ]
