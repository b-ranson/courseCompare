from django.contrib import admin

# Register your models here.

from .models import Courses, user, courseTaking
admin.site.register(user)
admin.site.register(Courses)
admin.site.register(courseTaking)