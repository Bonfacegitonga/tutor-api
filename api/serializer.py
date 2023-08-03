from rest_framework import serializers
from .models import Tutor, Module, Course, Content
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class TutorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
       model = Tutor
       fields = ['url','about', 'user']

class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Module
        fields = ['title', 'description']



class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    module= ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['url', 'title', 'tutor', 'price', 'overview', 'created','module']


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        field = ['item']


class ModuleWithContentsSerializer(serializers.HyperlinkedModelSerializer):
    contents = ContentSerializer(many=True)
    class Meta:
        model = Module
        fields = ['title', 'description', 'contents']


class ContentWithModuleSerializers(serializers.HyperlinkedModelSerializer):
    modules = ModuleWithContentsSerializer(many=True)
    class Meta:
        model = Course
        fields=['url', 'title', 'tutor', 'price', 'overview', 'created','modules']