from django.shortcuts import render
from django.http import HttpResponse
from .models import CallTrends
from django.db.models import Q
from django.contrib.admin import AdminSite
import json
from datetime import datetime, timedelta

def trends(request):
    trends = CallTrends.objects.all()
    admin_site = AdminSite()
    return render(request,'trends.html', {
        'trends':trends,        
        'admin_site': admin_site,
        })

def trends_search(request):   
    q = None
    q = request.GET.get('q')   
    if q:
        trends = CallTrends.objects.filter(Q(Time__icontains = q) | Q(Calls__icontains = q) | Q(Abnd__icontains = q))
        if not trends.exists():
            trends = None
    else:
        trends = CallTrends.objects.all()
    admin_site = AdminSite()
    return render(request,'trends.html', {
        'trends':trends,        
        'admin_site': admin_site,
        'q' : q,
        })

def graph_static(request):    
    trends = CallTrends.objects.all().order_by('Time').reverse()[:15]    
    trends = sorted(trends, key=lambda x: x.Time)
    datapoints = []
    datapoints2 = []
    for trend in trends:
        datapoints.append({'label': trend.Time, 'y': trend.Calls})
        datapoints2.append({'label': trend.Time, 'y': trend.Abnd})
    return render(request, 'graph_static.html', { "datapoints" : datapoints, "datapoints2": datapoints2 })

def graph_dynamic(request):
    trends = CallTrends.objects.all()    
    datapoints = []
    datapoints2 = []
    for trend in trends:
        datapoints.append({'x': trend.Time, 'y': trend.Calls})
        datapoints2.append({'x': trend.Time, 'y': trend.Abnd})
    return render(request, 'graph_dynamic.html', { "datapoints" : datapoints, "datapoints2": datapoints2 })
  
def get_datapoints(request):
    trends = CallTrends.objects.all().order_by('Time').reverse()[:15]    
    trends = sorted(trends, key=lambda x: x.Time)
    datapoints = []
    datapoints2 = []    
    for trend in trends:
        time_to_add_str = trend.Time
        hours, minutes, seconds = map(int, time_to_add_str.split(':'))
        current_date_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        current_date_time += timedelta(hours=hours, minutes=minutes, seconds=seconds)
        epoch_time = int(current_date_time.timestamp() * 1000)
        datapoints.append({'x': epoch_time, 'y': trend.Calls})
        datapoints2.append({'x': epoch_time, 'y': trend.Abnd})         
    data = {
        'datapoints_1':datapoints,
        'datapoints_2':datapoints2,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")   