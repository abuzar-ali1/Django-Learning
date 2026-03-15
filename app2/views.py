from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Profile , HackathonIdea , Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome in the Home of git Django Project</h1>")


def get_all_profiles(request):
    profile_list = list(Profile.objects.values())
    return JsonResponse({ "Profiles" : profile_list})


def get_all_hacks(request):
    Hackthons  = list(HackathonIdea.objects.values())
    return JsonResponse({ 'Hackothons' :Hackthons})


def filtererd_data(request):
    data = list(HackathonIdea.objects.filter(is_free_entry = True).values())
    return JsonResponse({'data' : data})


def id_base_data(request,  id ):
    result = HackathonIdea.objects.filter(id=id).values().first()
    if result:
        return JsonResponse({'data'  : result})
    else:
        return JsonResponse({'error' : 'Idea NOT FOUND ! Try again'} , status=404)


# an object
def student_detail(request , pk):
    stu  = Student.objects.get(id  = pk)
    serilizer = StudentSerializer(stu )
    # json_data = JSONRenderer().render(serilizer.data)
    # return HttpResponse(json_data , content_type = 'application/json')
    # Simple using of the JsonResponse
    return JsonResponse(serilizer.data)

# Query set
def students(request):
    stu  = Student.objects.all()
    serilizer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data , content_type = 'application/json')
    # mosltly we use JsonResponse to return a json
    # return JsonResponse(serilizer.data , safe=False)

@csrf_exempt
def student_create(request):
    if request.method  == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data is Created!'}
            return JsonResponse(res)
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data , content_type = 'application/json')
            


def get_student(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id' , None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type = 'application/json')    
    stu =  Student.objects.all()        
    serializer = StudentSerializer(stu , many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data , content_type = 'application/json')     
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id' , None)
        stu = Student.objects.get(id=id)
        serializer = Student.objects.get(stu , data=python_data)
        if serializer.valid():
            serializer.save()
            res = {'msg' : 'Data is successfully Updated'}
            return JsonResponse(res) 
