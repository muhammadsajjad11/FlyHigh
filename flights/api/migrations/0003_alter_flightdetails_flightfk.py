# Generated by Django 3.2.11 on 2022-01-20 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_flight_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetails',
            name='flightfk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flightdetails', to='api.flight'),
        ),
    ]
