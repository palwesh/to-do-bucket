from django.contrib import admin

# Register your models here.

from todobucket.models import Bucket, Todo

admin.site.register(Bucket)
admin.site.register(Todo)
