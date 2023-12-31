from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )
    bio = models.TextField()
    enrollment_date = models.DateField()

    def __str__(self):
        return f"Profile of {self.user.username}"


class Tutor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="tutor_profile"
    )
    overview = models.CharField(max_length=100)
    about = models.TextField()
    email = models.EmailField()
    tutor_first_name = models.CharField(max_length=100)
    tutor_last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Profile of {self.user.first_name}"


class Course(models.Model):
    title = models.CharField(max_length=200)
    overview = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, related_name="courses_created"
    )
    students = models.ManyToManyField(User, blank=True, related_name="courses_joined")
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    module = models.ForeignKey(
        Module, related_name="contents", on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"model__in": ("text", "video", "image", "file")},
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey("content_type", "object_id")


class ItemBase(models.Model):
    owner = models.ForeignKey(
        Tutor, related_name="%(class)s_related", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to="files")


class Image(ItemBase):
    file = models.FileField(upload_to="images")


class Video(ItemBase):
    url = models.URLField()


# class Tution(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     enrollment_price =  models.DecimalField(max_digits=8, decimal_places=2)
#     tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutions')

#     def __str__(self):
#         return self.name
