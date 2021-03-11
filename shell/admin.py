# coding:utf-8
from django.contrib import admin

# Register your models here.
from shell import models

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','manager')
class HostAdmin(admin.ModelAdmin):
    list_display = ('host_name','ip','system')


admin.site.register(models.Department,DepartmentAdmin)
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.CampusFiled)

admin.site.site_header="CMDB"
admin.site.site_title="CMDB"
admin.site.index_title="欢迎你"