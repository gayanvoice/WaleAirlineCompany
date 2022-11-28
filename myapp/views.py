from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


# Create your views here.
def booking_details(request):
    cursor = connection.cursor()
    cursor.execute('''select p.passport_no, concat(p.surname, ' ', p.other_names) full_name,
       f.origin, f.departure_time, f.destination, f.arrival_time, c.name,
       c.price, concat(a.airplane_number, '-', a.manufacturer_name, ' ',
           a.model_name, '/', a.sub_model_name) airplane, b.status, b.type
from myapp_booking b
    left join myapp_flightschedule f on f.flight_schedule_id = b.flight_schedule_id
left join myapp_passenger p on p.passenger_id = b.passenger_id
left join myapp_class c on c.class_id = b.class_id_id
left join myapp_airplane a on a.airplane_id = f.airplane_id
where b.status in ('RESERVE')
''')
    rows = cursor.fetchall()
    return render(request, 'report/booking_details.html', {'rows': rows})


def airplane_pilot_details(request):
    cursor = connection.cursor()
    cursor.execute('''select concat(a.airplane_number, ' ', a.manufacturer_name, ' ', a.model_name, ' ', a.sub_model_name) airplane,
       concat(e.surname, ' ', e.other_names) employee, e.pilot_rating from myapp_airplane a
right join myapp_employee e on e.airplane_id = a.airplane_id
where e.job_name in ('PILOT')''')
    rows = cursor.fetchall()
    return render(request, 'report/airplane_pilot_details.html', {'rows': rows})


def passenger_bookings(request):
    cursor = connection.cursor()
    cursor.execute('''select concat(p.passport_no, ' - ', p.surname, ' ', p.other_names) passenger,
       b.type, f.origin, f.destination,
       concat(a.manufacturer_name, ' ', a.model_name, ' ', a.sub_model_name) airplane
from myapp_booking b
left join myapp_passenger p on p.passenger_id = b.passenger_id
left join myapp_flightschedule f on f.flight_schedule_id = b.flight_schedule_id
left join myapp_airplane a on a.airplane_id = f.airplane_id''')
    rows = cursor.fetchall()
    return render(request, 'report/passenger_bookings.html', {'rows': rows})
