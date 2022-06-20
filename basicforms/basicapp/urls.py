from django.contrib import admin
from django.urls import path, re_path
from basicapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_name_view', views.form_name_view, name='form_name'),
    #re_path(r'\d', views.regex, name='regex'),
]
