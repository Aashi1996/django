from django.urls import path
from left_diamond import views

urlpatterns=[
    path("",views.left_diamond,name="left_diamond")
    ]
