from django.contrib import admin

from .models import FileCategory, FileUpload

# Register your models here.
admin.site.register(FileCategory)
admin.site.register(FileUpload)
