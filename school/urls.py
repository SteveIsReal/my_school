from django.urls import path

from . import views

urlpatterns = [
    path("", views.student_add, name="student_add"),
    path("success/", views.success, name="success")
]
