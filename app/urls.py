from app.views import *
from django.urls import path

app_name='person'

urlpatterns=[
    path('jspiders/',jspiders,name='jspiders'),
]