from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, home

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Use the built-in LogoutView
    path('register/', register, name='register'),
]
