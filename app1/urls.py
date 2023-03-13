from app1.views import *
from django.urls import path

app_name='special'
urlpatterns=[
    path('pyspiders/',pyspiders,name='pysiders'),
]