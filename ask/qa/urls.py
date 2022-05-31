from django.conf.urls import url, include
from qa.views import test                                                       
                                                                                
urlpatterns = [                                       
    url(r'^', test)
]
