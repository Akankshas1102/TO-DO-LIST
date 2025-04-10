from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('toggle/<int:task_id>/', views.toggle, name='toggle'),
]
