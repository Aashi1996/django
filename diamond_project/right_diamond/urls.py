from django.urls import path
from right_diamond import views

urlpatterns=[
    path("",views.right_diamond,name="right_diamond")
    ]
