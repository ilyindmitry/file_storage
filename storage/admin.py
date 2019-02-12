from django.contrib import admin
from .models import UserFile

@admin.register(UserFile)
class BlogAdmin(admin.ModelAdmin):
    fields = ['upload_datetime', 'user', 'file', 'status']
