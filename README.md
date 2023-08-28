# Django Rest Framework Project - Online Learning Platform📚🎓(project under development 35% done)

Welcome to the README for our Django Rest Framework project - an Online Learning Platform! This platform offers a wide range of features for both teachers and students, including user management, course management, live tutoring sessions, and payment handling.

## Table of Contents
1. [Authentication and User Management](#1-authentication-and-user-management)
2. [Courses](#2-courses)
3. [Live Tutoring](#3-live-tutoring)
4. [Payments](#4-payments)

## 1. Authentication and User Management
This section covers the endpoints related to user registration, authentication, and user profile management.

- `POST /api/register`: Register a new user (teacher or student).
- `POST /api/login`: User login to obtain an access token for subsequent API calls.
- `GET /api/profile`: Get the user's profile information.
- `PUT /api/profile`: Update the user's profile information.
- `GET /api/courses`: Get a list of available courses.

## 2. Courses
Manage courses as a teacher or enroll in courses as a student.

- `GET /api/courses/{courseId}`: Get details about a specific course.
- `POST /api/courses`: Create a new course (for teachers).
- `PUT /api/courses/{courseId}`: Update course details (for teachers).
- `DELETE /api/courses/{courseId}`: Delete a course (for teachers).
- `POST /api/courses/{courseId}/enroll`: Enroll a student in a course.
- `GET /api/courses/{courseId}/lectures`: Get a list of lectures in a course.
- `POST /api/courses/{courseId}/lectures`: Add a new lecture to a course (for teachers).

## 3. Live Tutoring
Facilitate live tutoring sessions.

- `POST /api/tutoring/schedule`: Schedule a live tutoring session (for teachers).
- `GET /api/tutoring/sessions`: Get a list of upcoming tutoring sessions (for teachers and students).
- `POST /api/tutoring/sessions/{sessionId}/join`: Join a live tutoring session (for students and teachers).
- `POST /api/tutoring/sessions/{sessionId}/end`: End a live tutoring session (for teachers).

## 4. Payments
Handle course payments.

- `POST /api/payments/purchase`: Allow students to purchase a course.
- `GET /api/payments/history`: Get payment history for a user (for teachers and students).

## Getting Started
To get started with this project, follow these steps:

1. Clone the repository: `git clone https://github.com/Bonfacegitonga/tutor-api`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser for admin access: `python manage.py createsuperuser`
7. Start the development server: `python manage.py runserver`

## Contributing
I welcome contributions to improve and expand this project. Feel free to open issues or submit pull requests.


*Note: Replace `{courseId}` and `{sessionId}` with actual IDs when making requests.* 
