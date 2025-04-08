from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm, TeacherForm

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'student_side/index.html', {"form":form})

def success(request):
    return render(request, 'student_side/success.html')

