from django.urls import path
from factorial import views

urlpatterns=[
    path("",views.factorial,name="factorial")
    ]
