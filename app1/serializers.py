from .models import Student
from rest_framework import serializers




class StudentSerializer(serializers.ModelSerializer):
    # name  = serializers.CharField( max_length=50 , read_only=True) 

    class Meta:
        model = Student 
        fields =  ['id', 'name' , 'email' , 'city']
    # read_only_field = ['name' , 'roll']
    # extra_keys = {'name' : {read_only : True}}

    def validate(self,  data):
        name = data.get('name')

        if name[0].lower() != 'a':
            raise serializers.ValidationError('THe name mus tbe start form the Latter A')
        return data

