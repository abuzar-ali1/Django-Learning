from django.shortcuts import render , get_object_or_404
import io
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from .models import Student

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




@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        
        # If a body is provided, parse it for an ID
        if json_data:
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            student_id = python_data.get('id', None)
            
            if student_id is not None:
                stu = Student.objects.get(id=student_id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
                
        # If no body or no ID provided, return all students
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is Created!'}
            return JsonResponse(res)
            
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        student_id = python_data.get('id', None)
        
        stu = Student.objects.get(id=student_id)
        serializer = StudentSerializer(stu, data=python_data)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is successfully Updated'}
            return JsonResponse(res)
            
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        student_id = python_data.get('id')
        
        stu = Student.objects.get(id=student_id)
        stu.delete()
        res = {'msg': 'Data is successfully Deleted'}
        return JsonResponse(res)

