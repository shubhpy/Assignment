from django.urls import re_path
from mainApp import views

urlpatterns=[
    re_path(r'^$',views.landing,name='landing-page'),
    re_path(r'^login/',views.userLogin,name='login'),    
    re_path(r'^register/',views.register,name='register'),
    re_path(r'^getAddress/',views.getAddress,name='getAddress'),    
]
