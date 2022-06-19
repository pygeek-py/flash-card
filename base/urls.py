from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('del/<str:pk>/', views.delete, name="delete"),
    
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]