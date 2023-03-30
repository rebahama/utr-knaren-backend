from django.contrib import admin
from .models import Post
from .countmodel import Calculator


admin.site.register(Post)
admin.site.register(Calculator)
