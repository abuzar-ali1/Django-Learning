from django.contrib import admin
from .models import Profile , HackathonIdea ,Teacher , Student
# Register your models here.

admin.site.register(Profile)
admin.site.register(HackathonIdea)
admin.site.register(Teacher)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =['id' , 'name' , 'roll' , 'city']