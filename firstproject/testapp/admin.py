from django.contrib import admin
from testapp.models import Employee
from testapp.models import Student

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):  #Employee model  
    list_display=['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)

class StudentAdmin(admin.ModelAdmin):    #student model
    list_display=['sno','sname','subjects','percentage']

admin.site.register(Student,StudentAdmin)