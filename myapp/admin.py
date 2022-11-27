from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Airplane
from .models import Employee
from .models import Passenger
from .models import FlightSchedule
from .models import EmployeeSchedule
from .models import Class
from .models import Seat
from .models import Booking

# Register your models here.





admin.site.register(Airplane)
admin.site.register(Employee)
admin.site.register(Passenger)
admin.site.register(FlightSchedule)
admin.site.register(EmployeeSchedule)
admin.site.register(Class)
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.unregister(Group)
admin.site.unregister(User)