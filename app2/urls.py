from django.urls import path
from . import views 
from .views import MyTodo
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/profiles/', views.get_all_profiles),
    path('' , views.welcome),
    path('api/ideas/' , views.get_all_hacks),
    path('api/ideas/free/' , views.filtererd_data),
    path('api/ideas/<int:id>/' , views.id_base_data ),
    path('stuinfo/<int:pk>' , views.student_detail ),
    path('stuinfo/' , views.students),
    path('stucreate/' , views.student_create),
    path('studentapi/' , views.get_student),
    path('todo/' , csrf_exempt(views.MyTodo.as_view())),
    path('todos/' , views.todos),


    # ... your other urls
]