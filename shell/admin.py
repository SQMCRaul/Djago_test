# coding:utf-8
from django.contrib import admin
from shell import models
from shell.utils import zabbix
from shell.utils import get_host

# Register your models here.

token=zabbix.get_token()


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','manager')



    # memory.short_description = 'CPU使用率'
    # cpu.allow_tags=True #解析html格式
    # cpu.admin_order_field='cpu'
class HostAdmin(admin.ModelAdmin):
    list_display = ('host_name','ip','system','campus_filed','app','department')

    def CPU(self,request):
        return token

    def memory(self,request):
        return token

    CPU.short_description = 'CPU使用率'
    memory.short_description='内存使用率'
    search_fields = ('host_name','system')  #搜索字段
    # list_filter = ('campus_filed',) #过滤字段
    list_per_page = 10
    list_editable = ('ip','campus_filed')

admin.site.register(models.Department,DepartmentAdmin)
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.CampusFiled)
admin.site.register(models.Monitor)


admin.site.site_header="CMDB"
admin.site.site_title="CMDB"
admin.site.index_title="欢迎你"
