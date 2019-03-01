from django.urls import path
from django.conf.urls import include
from mainapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('projects/', include('projects.urls')),
]
