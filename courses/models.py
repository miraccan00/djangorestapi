from django.db import models
from django.db.models.fields import CharField, SlugField

class Author(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    work = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug =models.SlugField(unique=True)

class CourseContent(models.Model):
    name = models.CharField(max_length=40)
    videoname = models.CharField(max_length=40)
    videourl = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    coursecontent = models.ForeignKey(CourseContent, on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self):
        return self.name
