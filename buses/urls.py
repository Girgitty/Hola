from django.urls import path
from . import views

urlpatterns = [
    # Bus registration flow
    path('registration/', views.bus_registration_view, name='bus_registration'),
    path('complete-profile/', views.complete_profile_view, name='complete_profile'),
    path('payment/<int:registration_id>/', views.payment_view, name='payment'),

    # Bus schedules and routes
    path('schedules/', views.view_schedules, name='view_schedules'),
    path('routes/', views.view_routes, name='view_routes'),

    # User registrations management
    path('my-registrations/', views.my_registrations_view, name='my_registrations'),
    path('cancel-registration/<int:registration_id>/', views.cancel_registration_view, name='cancel_registration'),

    # Admin/Authority views
    path('manage-buses/', views.manage_buses_view, name='manage_buses'),
    path('add-bus/', views.add_bus_view, name='add_bus'),
    path('edit-bus/<int:bus_id>/', views.edit_bus_view, name='edit_bus'),
    path('delete-bus/<int:bus_id>/', views.delete_bus_view, name='delete_bus'),

    # Bus schedules management
    path('manage-schedules/', views.manage_schedules_view, name='manage_schedules'),
    path('add-schedule/', views.add_schedule_view, name='add_schedule'),
    path('edit-schedule/<int:schedule_id>/', views.edit_schedule_view, name='edit_schedule'),
]