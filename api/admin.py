from django.contrib import admin
from .models import Course, Module, Tutor


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
    search_fields = ['title', 'overview']
    inlines = [ModuleInline]
    

admin.site.register(Tutor)