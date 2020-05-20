from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^update/$', views.UpdateProfile.as_view(), name='update'),
]