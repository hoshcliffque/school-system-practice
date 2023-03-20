from django.db import models
from courses.models import Course


class Person(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    date_of_join = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    

class Student(Person):
    parent_name = models.CharField(max_length=255, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name="students", null=True, blank=True)

class Teacher(Person):
    courses = models.ManyToManyField(Course, related_name="teachers", null=True, blank=True)