from django.urls import path
from app2.views import get_all_profiles , welcome

urlpatterns = [
    path('api/profiles/', get_all_profiles),
    path('' , welcome)
    # ... your other urls
]