from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name="index"),
    path('registration/', views.registration ,name="registration"),
    path('login/', views.log_in ,name="log_in"),
    path('home/', views.home ,name="home"),
    path('log_out/', views.log_out ,name="log_out"),
    
]
