from django.contrib import admin
from .models import CallTrends

class CallTrendsAdmin(admin.ModelAdmin):
    list_display =('Time','Calls','Abnd')
    search_fields = ['Time', 'Calls','Abnd']
    ordering = ('Time',)

admin.site.register(CallTrends,CallTrendsAdmin)
