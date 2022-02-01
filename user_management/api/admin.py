from django.contrib import admin
from .models import StudentTbl
# Register your models here.


@admin.register(StudentTbl)
class StudentAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'mobile', 'city', 'userid', 'password']