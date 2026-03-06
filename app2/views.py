from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Profile
# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome in the Django Project</h1>")


def get_all_profiles(request):
    profile_list = list(Profile.objects.values())
    return JsonResponse({ "Profiles" : profile_list})

