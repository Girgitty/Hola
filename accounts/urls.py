from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # ADDED: separate student signup
    path('student-register/', views.student_register, name='student_register'),
    # Use custom login view to enable success messages
    path('login/', views.StudentLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]