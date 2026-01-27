from django.contrib import admin
from .models import Post,Employee
@admin.register(Post)
class PostAdmiin(admin.ModelAdmin):
    list_display = ['title','slug','body','status']

@admin.register(Employee)    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name','email'] 