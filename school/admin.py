from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

@admin.register(Student)
class AdminStudetn(admin.ModelAdmin):
    list_display = ['name','grade']

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ['name']
    
