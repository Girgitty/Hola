from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Bus(models.Model):
    bus_number = models.CharField(max_length=20, unique=True)
    bus_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    # whether this bus is available for student bookings
    is_available = models.BooleanField(default=True)
    driver_name = models.CharField(max_length=100)
    driver_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.bus_number} - {self.bus_name}"


class Route(models.Model):
    route_name = models.CharField(max_length=100)
    start_point = models.CharField(max_length=200)
    end_point = models.CharField(max_length=200)
    stops = models.TextField(help_text="Comma separated list of stops", default='', blank=True)
    # distance = models.FloatField()  # TEMPORARILY COMMENTED OUT
    # Set a default so existing rows get a sensible value when migrating
    estimated_time = models.IntegerField(help_text="Estimated time in minutes", default=0)

    def __str__(self):
        return self.route_name


class BusSchedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    # track how many seats are available for the schedule
    available_seats = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.bus.bus_number} - {self.route.route_name} - {self.departure_time}"


# ADD THIS MISSING MODEL
class Registration(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(BusSchedule, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ['user', 'schedule']

    def __str__(self):
        return f"{self.user.username} - {self.schedule}"


class FleetSettings(models.Model):
    """A tiny singleton model to store fleet-level settings like how many buses
    are available for student use. Keeping it in the DB makes it editable via
    the admin UI.
    """
    available_buses = models.PositiveIntegerField(default=0, help_text="How many buses can be allocated for student use")

    def __str__(self):
        return f"Fleet settings (available buses: {self.available_buses})"

    class Meta:
        verbose_name = "Fleet Settings"

