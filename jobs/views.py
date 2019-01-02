"""
Views for Jobs application.
"""
from django.shortcuts import render
from .models import Job


def home(request):
    """Home page render"""
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
