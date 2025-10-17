from django.urls import path
from . import views

app_name = 'buses'

urlpatterns = [
    path('', views.bus_list_view, name='bus_list'),
    path('manage/', views.manage_buses_view, name='manage_buses'),
    path('add/', views.add_bus_view, name='add_bus'),
    path('edit/<int:bus_id>/', views.edit_bus_view, name='edit_bus'),
    path('delete/<int:bus_id>/', views.delete_bus_view, name='delete_bus'),
    path('schedules/', views.view_schedules, name='schedules'),
    path('add-schedule/', views.add_schedule_view, name='add_schedule'),
    path('manage-schedules/', views.manage_schedules_view, name='manage_schedules'),
    path('add-schedule/<int:schedule_id>/edit/', views.edit_schedule_view, name='edit_schedule'),
    path('bus/<int:bus_id>/', views.bus_detail_view, name='bus_detail'),
]
