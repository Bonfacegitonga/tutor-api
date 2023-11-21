from ninja import NinjaAPI
from typing import List, Optional
from .schema import TutorSchema, CourseSchema
from .models import Tutor, Course

api = NinjaAPI()

@api.get('tutors/', response=List[TutorSchema])
def get_all_tutors(request):
    tutors= Tutor.objects.all()
    return tutors

@api.get('courses/',  response=List[CourseSchema])
def get_courses(request):
        courses = Course.objects.all()
        return courses