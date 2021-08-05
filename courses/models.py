from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    work = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class CourseContent(models.Model):
    name = models.CharField(max_length=40)
    videoname = models.CharField(max_length=40)
    videourl = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    coursecontent = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
