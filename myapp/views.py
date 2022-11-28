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


def pilot_schedule_by_month(request):
    cursor = connection.cursor()
    cursor.execute('''select
    DATE(fs.departure_time) date,
    concat(e.surname, ' ', e.other_names) employee,
    concat(a.manufacturer_name, ' ', a.model_name, ' ', a.sub_model_name, ' ', a.airplane_number) airplane,
    concat(fs.origin, ' (', fs.departure_time, ')' ' ', fs.destination, ' (' ,fs.departure_time, ')') airport, fs.status
from myapp_employeeschedule es
left join  myapp_employee e on e.employee_id = es.employee_id
left join  myapp_flightschedule fs on fs.flight_schedule_id = es.flight_schedule_id
left join myapp_airplane a on a.airplane_id = e.airplane_id
where e.job_name in ('PILOT')
order by fs.departure_time asc''')
    rows = cursor.fetchall()
    return render(request, 'report/pilot_schedule_by_month.html', {'rows': rows})


def number_of_passengers_by_flight(request):
    cursor = connection.cursor()
    cursor.execute('''select
    concat(a.manufacturer_name, ' ', a.model_name, ' ', a.sub_model_name, ' - ', a.airplane_number) airplane,
    (select count(*) from myapp_booking b
                     left join myapp_flightschedule f on f.flight_schedule_id = b.flight_schedule_id
                     where f.airplane_id = a.airplane_id and b.status in ('RESERVE')) passenger_count
from myapp_airplane a''')
    rows = cursor.fetchall()
    return render(request, 'report/number_of_passengers_by_flight.html', {'rows': rows})


def number_of_working_hours_by_pilot(request):
    cursor = connection.cursor()
    cursor.execute('''select b.employee_id, b.surname, b.other_names, cast(SEC_TO_TIME(total_time) as char) time_difference from (
select a.employee_id, a.surname, a.other_names, sum(a.time_difference) AS total_time
from (select e.employee_id,
             e.surname,
             e.other_names,
             TIME_TO_SEC((select timediff(arrival_time, departure_time) time_difference
              from myapp_flightschedule where flight_schedule_id in (es.flight_schedule_id))) time_difference
      from myapp_employee e
               right join myapp_employeeschedule es on es.employee_id = e.employee_id
      where e.job_name in ('PILOT')) a
group by a.employee_id) b''')
    rows = cursor.fetchall()
    return render(request, 'report/number_of_working_hours_by_pilot.html', {'rows': rows})


def destinations_and_bookings(request):
    cursor = connection.cursor()
    cursor.execute('''select concat(a.manufacturer_name, ' ', a.model_name, ' ', a.sub_model_name, ' - ', a.airplane_number) airplane,
       fs.origin, fs.departure_time, fs.destination, fs.arrival_time, status
from myapp_flightschedule fs
left join myapp_airplane a on a.airplane_id = fs.airplane_id''')
    rows = cursor.fetchall()
    return render(request, 'report/destinations_and_bookings.html', {'rows': rows})
