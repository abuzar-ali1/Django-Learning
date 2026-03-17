from rest_framework import serializers
from .models import Student , Todo




class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  
    name  = serializers.CharField( max_length=50) 
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)    

    def create(self , valid_data):
        return Student.objects.create(**valid_data)

    def update(self , instance , validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.roll = validated_data.get('roll' , instance.roll)
        instance.city = validated_data.get('city' , instance.city)
        instance.save()
        return instance

class TodoSerializer(serializers.Serializer):
    id =  serializers.IntegerField(read_only=True)
    title = serializers.CharField( max_length=500)
    desc = serializers.CharField( max_length=1000)
    isDone =  serializer.BooleanField()


    def create(self , valid_data):
        return Todo.objects.create(**valid_data)
        
