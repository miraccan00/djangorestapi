from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Author,CourseContent
from .serializers import CourseSerializer,AuthorSerializer,CourseContentSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CourseContentView(viewsets.ModelViewSet):
    queryset = CourseContent.objects.all()
    serializer_class = CourseContentSerializer