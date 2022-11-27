from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def details(request):
    return render(request, 'custom/details.html')
