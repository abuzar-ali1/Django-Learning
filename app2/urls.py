from django.urls import path
from app2.views import get_all_profiles , welcome , get_all_hacks , filtererd_data

urlpatterns = [
    path('api/profiles/', get_all_profiles),
    path('' , welcome),
    path('api/ideas/' , get_all_hacks),
    path('api/ideas/free/' , filtererd_data)
    # ... your other urls
]