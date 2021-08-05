from django.contrib import admin
from .models import Course,Author,CourseContent

admin.site.register(CourseContent)
admin.site.register(Course)
admin.site.register(Author)
