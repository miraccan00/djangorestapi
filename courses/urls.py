from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseView)
router.register('author', views.AuthorView)
router.register('coursecontent', views.CourseContentView)


urlpatterns = [
    path('', include(router.urls)),

]
