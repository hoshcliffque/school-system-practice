from django.shortcuts import render, get_object_or_404
from .models import Student
from courses.models import Course, Class
from datetime import datetime

def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    courses = Course.objects.all()
    classes = Class.objects.filter(course__in=student.courses.all(), date__gte=datetime.now()).order_by('date')

    context = {
        'student': student,
        'courses': courses,
        'classes': classes
    }

    return render(request, "accounts/student_profile.html", context)