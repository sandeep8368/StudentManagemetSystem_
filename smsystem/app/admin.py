from django.contrib import admin
from app.models import studentModel
# Register your models here.


class studentModelAdmin(admin.ModelAdmin):
    list_display = ['name','roll','email','phone']
    
    
    
admin .site.register(studentModel,studentModelAdmin)