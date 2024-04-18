from django.urls import path
from full_diamond import views

urlpatterns=[
    path("",views.full_diamond,name="full_diamond")
    ]
