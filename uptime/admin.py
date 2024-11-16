from django.contrib import admin
from .models import ServerUptime

class ServerUptimeAdmin(admin.ModelAdmin):
    list_display =('HostName','HostIntIP','BootTime','UpTime')
    search_fields = ['HostName', 'HostIntIP']
    ordering = ('HostName',)

admin.site.register(ServerUptime,ServerUptimeAdmin)
