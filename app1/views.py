from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , JsonResponse
# Create your views here.


def home(request , message):
    return HttpResponse(f"<h1>{message}</h2>")




def greeting(request , username):
    result = {'message' : f'Welcome back {username}' , 'is_admin' : False}
    return JsonResponse(result)



def search(request):
    query =  request.GET.get('keyword')
    result = {"search_results_for": f'{query}', "items_found": 0}
    if query:

        return JsonResponse(result)
    else:

        message = "You did not provide a search query."

def about(request):
    return HttpResponse("This is the simple about section")
