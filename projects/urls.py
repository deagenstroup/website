from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projectindex, name='projectindex'),
    path('<str:name>', views.projectpage, name='projectpage')
]
