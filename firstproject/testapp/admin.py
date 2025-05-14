from django.contrib import admin
from testapp.models import Employee
from testapp.models import Student
from testapp.models import College
from testapp.models import Address

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):  #Employee model  
    list_display=['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)

class StudentAdmin(admin.ModelAdmin):    #student model
    list_display=['sno','sname','subjects','percentage']

admin.site.register(Student,StudentAdmin)

class CollegeAdmin(admin.ModelAdmin):
    list_display=['name','college_name','subjects','course','location','mobilenumber']

admin.site.register(College,CollegeAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display=['street','city','state','zip_code']

admin.site.register(Address,AddressAdmin)