from django.contrib import admin
from .models import ContactU,StudentApplication,FileUpload
# Register your models here.
admin.site.register(ContactU)
admin.site.register(StudentApplication)
admin.site.register(FileUpload)