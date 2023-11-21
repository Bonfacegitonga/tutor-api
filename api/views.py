from rest_framework import viewsets
from  rest_framework import permissions
from .serializer import TutorSerializer, CoursesSerializer, ContentWithModuleSerializers
from .models import Tutor, Course
# Create your views here.


# class TutorViewSet(viewsets.ModelViewSet):
#     queryset = Tutor.objects.all()
#     serializer_class = TutorSerializer
#     permission_classes  = [permissions.IsAuthenticated]


# class CourseViewSet(viewsets.ModelViewSet):
#     queryset=  Course.objects.all()
#     serializer_class = ContentWithModuleSerializers
#     permission_classes = [permissions.IsAuthenticated]


