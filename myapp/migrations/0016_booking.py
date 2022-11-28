# Generated by Django 4.1.3 on 2022-11-28 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('RESERVE', 'RESERVE')], default='RESERVE', max_length=10)),
                ('flight_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.flightschedule')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.passenger')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.seat')),
            ],
        ),
    ]