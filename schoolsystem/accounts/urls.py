from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:student_id>', views.student_profile, name="student_profile"),
]