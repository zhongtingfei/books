from django.urls import re_path
from .views import *


urlpatterns = [

    re_path('^$', V_index),
    re_path('^index/$', V_index),
    re_path("login/", V_login, name='login'),
    re_path("register/", V_register, name='register'),
    re_path('check/', V_check),
    re_path('test/', V_test),

]
