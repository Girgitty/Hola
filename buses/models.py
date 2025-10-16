from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bus, BusSchedule, Route, Registration
from django.db.models import Q


@login_required
def bus_registration_view(request):
    # Complete profile check (simplified)
    if not request.user.first_name or not request.user.last_name:
        messages.warning(request, 'Please complete your profile first.')
        return redirect('complete_profile')

    routes = Route.objects.all()
    selected_route = None
    schedules = None

    if request.method == 'POST':
        route_id = request.POST.get('route')
        schedule_id = request.POST.get('schedule')

        if route_id:
            selected_route = Route.objects.get(id=route_id)
            schedules = BusSchedule.objects.filter(bus__route_name=selected_route.route_name)

        if schedule_id:
            schedule = BusSchedule.objects.get(id=schedule_id)
            # Check if already registered
            if Registration.objects.filter(user=request.user, bus_schedule=schedule).exists():
                messages.error(request, 'You are already registered for this bus schedule.')
            elif schedule.available_seats > 0:
                registration = Registration(user=request.user, bus_schedule=schedule)
                registration.save()
                messages.success(request, 'Successfully registered for the bus!')
                return redirect('payment', registration_id=registration.id)
            else:
                messages.error(request, 'No available seats for this schedule.')

    return render(request, 'bus/registration.html', {
        'routes': routes,
        'selected_route': selected_route,
        'schedules': schedules
    })


@login_required
def complete_profile_view(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('bus_registration')

    return render(request, 'bus/complete_profile.html')


@login_required
def payment_view(request, registration_id):
    registration = Registration.objects.get(id=registration_id, user=request.user)

    if request.method == 'POST':
        # Simulate payment processing
        registration.payment_status = True
        registration.payment_amount = 50.00  # Fixed amount for demo
        registration.save()
        messages.success(request, 'Payment successful! Registration completed.')
        return redirect('dashboard')

    return render(request, 'bus/payment.html', {'registration': registration})