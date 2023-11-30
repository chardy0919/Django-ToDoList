from django.contrib import admin
from .models import List,Task,SubTask

# Register your models here.
admin.site.register([List,Task,SubTask])
