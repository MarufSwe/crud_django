from django.contrib import admin

from .models import *


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'emp_code', 'mobile', 'position']


class PositionAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
