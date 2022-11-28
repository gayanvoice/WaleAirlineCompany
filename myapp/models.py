from django.db import models


# Create your models here.
class Airplane(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    airplane_number = models.CharField(max_length=20)
    manufacturer_name = models.CharField(max_length=45)
    model_name = models.CharField(max_length=20)
    sub_model_name = models.CharField(max_length=20)

    def __str__(self):
        return self.airplane_number + ' - ' + self.manufacturer_name + '/' + self.model_name + '/' + self.sub_model_name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=45)
    other_names = models.CharField(max_length=45)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    pilot_rating = models.CharField(max_length=20, null=True)
    HOST = 'HOST'
    PILOT = 'PILOT'
    OTHER = 'OTHER'
    JOB_CHOICES = [
        (HOST, 'HOST'),
        (PILOT, 'PILOT'),
        (OTHER, 'OTHER')
    ]
    job_name = models.CharField(
        max_length=10,
        choices=JOB_CHOICES,
        default=OTHER,
    )
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.job_name + '/' + self.surname + ' ' + self.other_names


class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    passport_no = models.CharField(max_length=10)
    type = models.CharField(max_length=45)
    country_code = models.CharField(max_length=45)
    surname = models.CharField(max_length=200)
    other_names = models.CharField(max_length=20)
    national_status = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    id_no = models.IntegerField()
    profession = models.CharField(max_length=20)
    sex = models.BooleanField()
    place_of_birth = models.CharField(max_length=20)
    date_of_issue = models.DateField()
    date_of_expiry = models.DateField()
    authority = models.CharField(max_length=20)

    def __str__(self):
        return self.passport_no + ' - ' + self.country_code + '/' + self.surname + ' ' + self.other_names


class FlightSchedule(models.Model):
    flight_schedule_id = models.AutoField(primary_key=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    ARRIVE = 'ARRIVE'
    DEPARTURE = 'DEPARTURE'
    CANCEL = 'CANCEL'
    STATUS_CHOICES = [
        (ARRIVE, 'Arrive'),
        (DEPARTURE, 'Departure'),
        (CANCEL, 'Cancel')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ARRIVE,
    )

    def __str__(self):
        return str(self.flight_schedule_id) + ' - ' + self.origin + ' (' + str(
            self.departure_time.date()) + ') / ' + self.destination + ' (' + str(self.arrival_time.date()) + ')'


class EmployeeSchedule(models.Model):
    employee_schedule_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    flight_schedule = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE)
    FULL_TIME = 'FULL_TIME'
    PART_TIME = 'PART_TIME'
    STATUS_CHOICES = [
        (FULL_TIME, 'FULL_TIME'),
        (PART_TIME, 'PART_TIME')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=FULL_TIME,
    )

    def __str__(self):
        return str(self.employee_schedule_id) + ' - ' + str(self.employee_id) + '/' + str(self.flight_schedule_id)


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return str(self.airplane_id) + ' - ' + self.name


class Booking(models.Model):
    book_id = models.AutoField(primary_key=True)
    flight_schedule = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    AVAILABLE = 'AVAILABLE'
    RESERVE = 'RESERVE'
    STATUS_CHOICES = [
        (AVAILABLE, 'AVAILABLE'),
        (RESERVE, 'RESERVE')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=RESERVE,
    )
    DIRECT = 'DIRECT'
    CONNECT = 'CONNECT'
    TYPE_CHOICES = [
        (DIRECT, 'DIRECT'),
        (CONNECT, 'CONNECT')
    ]
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=RESERVE
    )

    def __str__(self):
        return str(self.flight_schedule) + ' - ' + str(self.passenger)
