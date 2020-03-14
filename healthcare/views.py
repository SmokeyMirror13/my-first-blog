from django.shortcuts import render
from django.utils import timezone
from .models import Patients

def patient_list(request):
    patients = Patients.objects.all()
    return render(request, 'healthcare/patient_list.html', {'patients': patients})
