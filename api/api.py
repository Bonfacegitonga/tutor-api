from ninja import NinjaAPI
from typing import List, Optional
from .schema import TutorSchema, CourseSchema, CourseSchemaOut, CourseSchemaIn
from .models import Tutor, Course
from django.shortcuts import get_object_or_404
from ninja.security import django_auth



api = NinjaAPI(auth= django_auth, csrf=True)


@api.get('tutors/', response=List[TutorSchema])
def get_all_tutors(request):
    tutors= Tutor.objects.all()
    return tutors

@api.get('courses/',  response=List[CourseSchema])
def list_courses(request):
        courses = Course.objects.all()
        return courses


@api.get('courses/{course_id}',  response=CourseSchemaOut)
def get_course(request, course_id: int):
        course = get_object_or_404(Course, id=course_id)
        return course

@api.post('courses/')
def post_courses(request, payload: CourseSchemaIn):
    tutor_id = payload.tutor
    # Check if the user associated with the API key is a tutor
    tutor = Tutor.objects.filter(id=tutor_id).first()
    if not tutor:
        return {"message": "You do not have permission to create courses."}

    # Create the course
    course_data = payload.dict()
    course_data['tutor'] = tutor  # Assign the Tutor instance, not the ID

    course = Course.objects.create(**course_data)

    # Convert the course object to a dictionary for serialization
    course_dict = {
        "id": course.id,
        "title": course.title,
        "overview": course.overview,
        "description": course.description,
        "price": course.price,
        "tutor": course.tutor.id,
        "students": [student.id for student in course.students.all()],
        "created": course.created,
    }

    return {"message": "Course created successfully", "course": course_dict}


@api.delete('courses/{course_id}')
def delete_course(request, course_id: int):
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return {"success": True}