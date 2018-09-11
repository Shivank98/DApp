from django.http import HttpResponse
import datetime

def current_date_time(request):
    now  = datetime.datetime.now()
    htmlR = "<html><body> The time is %s<body><html>" % now
    return HttpResponse(htmlR)