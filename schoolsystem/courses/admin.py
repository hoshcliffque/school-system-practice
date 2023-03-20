from django.contrib import admin
from .models import Course, Class, Result

# Register your models here.
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Result)