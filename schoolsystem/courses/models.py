from django.db import models

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=7, primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course_code} - {self.title}"
    
class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="classes")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name_plural = "classes"

class Result(models.Model):
    student = models.ForeignKey("accounts.Student", on_delete=models.CASCADE, related_name="results")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="results")
    score = models.IntegerField()

    def __str__(self):
        return f"{self.course.title} - {self.student.name}: {self.score}"