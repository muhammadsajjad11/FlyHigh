# Generated by Django 3.2.11 on 2022-01-24 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_flightdetails_flightfk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetails',
            name='flightfk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.flight'),
        ),
    ]
