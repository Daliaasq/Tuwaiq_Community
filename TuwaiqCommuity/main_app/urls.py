from django.urls import path
from . import views

app_name= "main_app"

urlpatterns=[
    path('',views.welcome_page,name="welcome_page"),
    path('home/',views.home_page,name="home_page"),
    path('bootcamps/',views.bootcamps_page, name="bootcamps"),
    path('create/bootcamp/',views.create_bootcamp, name="create_bootcamp"),
]
