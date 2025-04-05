from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32)
    grade = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.grade}'

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    under_control_students = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, student : {self.under_control_students}'


