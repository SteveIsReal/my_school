
from django import forms
from .models import Student, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","grade"]

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name","under_control_students"]

