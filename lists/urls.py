from django.conf.urls import url, include
from django.contrib import admin
from lists import views

urlpatterns = [
    url(r'^', views.home_page, name='home_page'),
]
