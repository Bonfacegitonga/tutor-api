from ninja import ModelSchema
from typing import List, Optional
from .models import Tutor, Course, Module, Content, Text, File, Image, Video

class TutorSchema(ModelSchema):
    class Config:
        model = Tutor
        model_fields = ['tutor_first_name', 'tutor_last_name','email','overview', 'about']

class ContentSchema(ModelSchema):
    
    # content_object = ModelSchema(
    #     {
    #         'text': TextSchema,
    #         'file': FileSchema,
    #         'image': ImageSchema,
    #         'video': VideoSchema,
    #     },
    #     allow_dispatch=True,
    # )

    class Meta:
        model = Content
        fields = ['id', 'content_type', 'module']


class TextSchema(ModelSchema):
    class Meta:
        model = Text
        fields= '__all__'

class FileSchema(ModelSchema):
    class Meta:
        model = File
        fields= '__all__'

class ImageSchema(ModelSchema):
    class Meta:
        model = Image
        fields= '__all__'

class VideoSchema(ModelSchema):
    class Meta:
        model = Video
        exclude = ['id', 'owner',]

class ModuleSchema(ModelSchema):
    image: List[ImageSchema]
    file: List[FileSchema]
    video:List[VideoSchema]
    rich_content: TextSchema
    class Meta:
        model = Module
        fields = ['id', 'title', 'description', 'course']

class CourseSchema(ModelSchema):
    module: List[ModuleSchema]
    class Meta:
        model = Course
        fields = ['id', 'title', 'overview', 'description', 'price', 'tutor', 'students', 'created']

class CourseSchemaIn(ModelSchema):
    class Meta:
        model =Course
        fields = '__all__'