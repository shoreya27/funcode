
#from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='home'),
    path('word/', views.wordcount , name='wordcount'),
    path('aboutus',views.aboutus ,name='aboutus')
]
