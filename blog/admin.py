from django.contrib import admin
from .models import Post,Employee
@admin.register(Post)
class PostAdmiin(admin.ModelAdmin):
    list_display = ['title','slug','body','status']
    search_fields = ['title','body']
    prepopulated_fields ={'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy ='publish'
    ordering =['status','publish']


@admin.register(Employee)    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name','email']
    search_fields = ['last_name'] 