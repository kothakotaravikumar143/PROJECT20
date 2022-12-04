from django.urls import path
from app1.views import *
app_name='fasiha'
urlpatterns=[
    path('jas/',jas,name='jas')
]