# Generated by Django 4.1.3 on 2022-11-27 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_class_seat_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]