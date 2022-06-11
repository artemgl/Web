"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from qa import views

urlpatterns = [                                                                 
    url(r'^$', views.main_page),                                             
    url(r'^login/', login, {'template_name': 'login.html'}),                             
    url(r'^signup/', views.signup),                                       
    url(r'^question/(?P<pk>\d+)', views.question),                                
    url(r'^ask/', views.ask),                                
    url(r'^popular/', views.popular),                                      
#    url(r'^new/', include('qa.urls'))                                           
]
