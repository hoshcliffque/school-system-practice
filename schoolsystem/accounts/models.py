from django.db import models
from courses.models import Course, Result


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
    profile_picture = models.ImageField(upload_to="uploads/")

    def course_averages(self):
        results = Result.objects.filter(student=self)
        courses = self.courses.all()

        course_averages = {}

        for course in courses:
            course_averages[course.course_code] = 0

        
        for result in results:
            course_averages[result.course.course_code] += result.score
            

        for course in courses:
            total_results = Result.objects.filter(course=course, student=self).count()
            course_averages[course.course_code] = round(course_averages[course.course_code] / total_results, 2)


        return course_averages

class Teacher(Person):
    courses = models.ManyToManyField(Course, related_name="teachers", null=True, blank=True)