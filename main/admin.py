from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin
from .models import CustomGroup

# Register your models here.

from .models import Courses, MyCustomUser, CourseTaking
admin.site.register(MyCustomUser)
admin.site.register(Courses)
admin.site.register(CourseTaking)


#group = Group(name='BASEUSER')
#g1 = Group(name='PAIDUSER')
#group.save()
#g1.save()

