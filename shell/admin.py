# coding:utf-8
from django.contrib import admin

# Register your models here.
from shell import models
import random
from shell.utils import zabbix
token=zabbix.get_token('Admin','zabbix')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','manager','cpu')


    def cpu(self,obj):
        print(obj.name)
        print(token)
        itemid=zabbix.get_speed(token)
        return itemid
    cpu.short_description = 'CPU使用率'
    cpu.allow_tags=True #解析html格式
    cpu.admin_order_field='cpu'
class HostAdmin(admin.ModelAdmin):
    list_display = ('host_name','ip','system')


admin.site.register(models.Department,DepartmentAdmin)
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.CampusFiled)
admin.site.register(models.Monitor)


admin.site.site_header="CMDB"
admin.site.site_title="CMDB"
admin.site.index_title="欢迎你"