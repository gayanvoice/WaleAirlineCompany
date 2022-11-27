from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Airplane
from .models import Employee
from .models import Passenger

# Register your models here.


admin.site.register(Airplane)
admin.site.register(Employee)
admin.site.register(Passenger)
admin.site.unregister(Group)
admin.site.unregister(User)