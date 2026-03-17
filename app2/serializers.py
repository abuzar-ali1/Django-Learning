from rest_framework import serializers
from .models import Student , Todo

# Validators

def start_with_a(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError('Name shoulbe Start with A')
    return value    


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  
    name  = serializers.CharField( max_length=50 , validators=[start_with_a]) 
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



    def validate_roll(self , value):
        if value > 5000:
            raise serializers.ValidationError('Seat Full please Enter a roll less than 5000')
        return value


    def validate(self , data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'abuzar' and ct.lower() != 'lahore' :
            raise serializers.ValidationError('abuzar must be form Lahore')
        return data    


        
class TodoSerializer(serializers.Serializer):
    id =  serializers.IntegerField(read_only=True)
    title = serializers.CharField( max_length=500)
    desc = serializers.CharField( max_length=1000)
    is_done =  serializers.BooleanField()


    def create(self , valid_data):
        return Todo.objects.create(**valid_data)


    def update(self , instance, validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.desc = validated_data.get('desc' , instance.desc)
        instance.is_done = validated_data.get('is_done' , instance.is_done)
        instance.save()
        return instance




