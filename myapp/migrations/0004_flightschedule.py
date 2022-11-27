# Generated by Django 4.1.3 on 2022-11-27 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_employee_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightSchedule',
            fields=[
                ('flight_schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('ARRIVE', 'Arrive'), ('DEPARTURE', 'Departure'), ('CANCEL', 'Cancel')], default='ARRIVE', max_length=10)),
                ('airplane_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.airplane')),
            ],
        ),
    ]