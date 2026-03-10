from django.urls import path
from . import views 

urlpatterns = [
    path('api/profiles/', views.get_all_profiles),
    path('' , views.welcome),
    path('api/ideas/' , views.get_all_hacks),
    path('api/ideas/free/' , views.filtererd_data),
    path('api/ideas/<int:id>/' , views.id_base_data ),
    path('stuinfo/<int:pk>' , views.student_detail ),
    path('stuinfo/' , views.students)

    # ... your other urls
]