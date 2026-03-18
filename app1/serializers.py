from .models import Student
from rest_framework import serializers




class StudentSerializer(serializers.ModelSerailizer):
    class Meta:
        model = Student 
        
