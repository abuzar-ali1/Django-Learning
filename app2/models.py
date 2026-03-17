from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    city =  models.CharField(max_length=50)
    roll  = models.IntegerField()
    marks = models.IntegerField()
    state = models.CharField(max_length=50)
    commit = models.CharField( max_length=50 , default = 'nothing')

    def __str__(self):
        return self.name
    
     

class HackathonIdea(models.Model):
    title = models.CharField(max_length=100)
    core_tech = models.CharField( max_length=100)
    is_free_entry  = models.BooleanField()
    difficulty_level = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    Job_title = models.CharField(max_length=50)
    ID_NO : models.IntegerField()




    # Models for serialzers
class Student(models.Model):
    name  = models.CharField( max_length=50) 
    roll = models.IntegerField()
    city = models.CharField(max_length=50)    


class Todo(models.Model):
    title = models.CharField( max_length=500)
    desc = models.CharField( max_length=1000)
    is_done =  models.BooleanField()

