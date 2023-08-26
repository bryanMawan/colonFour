from django.urls import path
from .views import TestView, login_view, logout_view, register_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', TestView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    ]
