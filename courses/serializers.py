# This is our serializer page
from rest_framework import serializers
from .models import Course,Author,CourseContent,Category

class AuthorSerializer(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='author-detail')
    class Meta:
        model = Author
        # fields = ('__all__')
        fields = ('id','url','name','lastname','work','description')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'slug')

class CourseContentSerializer(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='author-detail')
    class Meta:
        model = CourseContent
        fields = ('id','url','name','videoname','videourl')
        

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'description', 'language', 'price','author' ,'category','coursecontent')