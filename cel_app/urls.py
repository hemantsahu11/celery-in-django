from django.urls import path, include
from . import views

urlpatterns = [
    path('test_task/', views.test, name='test'),
    path('', views.home, name='home'),
    path('send_mail/', views.send_main_to_all, name='send_mail'),
]