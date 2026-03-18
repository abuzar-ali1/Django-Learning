from django.urls import path
from . import views


urlpatterns = [
    path('home/' , views.home , {"message" : "This is the Home page and This is comming form the passing the data to the Url as  a message from the django project "}),
    path('api/greeting/<username>/' , views.greeting),
    path('api/search/' , views.search),
    path('about/' , views.about),
    path('stuapi/', views.StudentAPI.as_view(), name='student_api'),
]



