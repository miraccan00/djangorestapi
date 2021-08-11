# This is our serializer page
from rest_framework import serializers
from .models import Course,Author,CourseContent


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'description', 'author', 'language', 'price','coursecontent')

class AuthorSerializer(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='author-detail')
    class Meta:
        model = Author
        # fields = ('__all__')
        fields = ('id','url','name','lastname','work','description')

class CourseContentSerializer(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='author-detail')
    class Meta:
        model = CourseContent
        # fields = ('__all__')
        fields = ('id','url','name','videoname','videourl')
        