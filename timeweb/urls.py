"""timeweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
#from  timeweb.views import current_date_time
from . import views
"""urlpatterns = [
    path('admin/', admin.site.urls),
    path('time')

]
"""
urlpatterns = [
        url(r'^time/$', views.current_date_time), 
        # http://127.0.0.1:8000/time will send a request to views.current_date_time.
        # and views.current_date_time will Response by sending current date and time as in current_date_time function.



]
