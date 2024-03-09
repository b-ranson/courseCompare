from django.contrib import admin

# Register your models here.

from .models import Courses, MyCustomUser, CourseTaking
admin.site.register(MyCustomUser)
admin.site.register(Courses)
admin.site.register(CourseTaking)