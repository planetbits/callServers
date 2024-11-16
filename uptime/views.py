from django.shortcuts import render
from .models import ServerUptime
from django.db.models import Q
from django.contrib.admin import AdminSite

def uptime(request):
    servers = ServerUptime.objects.all()
    admin_site = AdminSite()
    return render(request,'uptimes.html', {
        'servers':servers,        
        'admin_site': admin_site,
        })

def uptime_search(request):   
    q = None
    q = request.GET.get('q')   
    if q:
        servers = ServerUptime.objects.filter(Q(HostName__icontains = q) | Q(HostIntIP__icontains = q))
        if not servers.exists():
            servers = None
    else:
        servers = ServerUptime.objects.all()
    admin_site = AdminSite()
    return render(request,'uptimes.html', {
        'servers':servers,        
        'admin_site': admin_site,
        'q' : q,
        })
