# Generated by Django 4.1.3 on 2022-11-28 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_employeeschedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='passenger_id',
            new_name='passenger',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='seat_id',
            new_name='seat',
        ),
    ]
