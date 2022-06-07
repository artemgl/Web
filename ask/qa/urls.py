from django.conf.urls import url, include
from qa.views import *
                                                                                
urlpatterns = [                                       
    url(r'^', main_page),
    url(r'^popular/', popular),
    url(r'^question/(?P<id>\d+)/', question)
]
