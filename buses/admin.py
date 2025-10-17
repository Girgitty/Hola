from django.contrib import admin
from .models import Bus, Route, BusSchedule, Registration
from .models import FleetSettings

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ["id", "bus_number"]
    search_fields = ["bus_number"]
    list_filter = ["is_available"]
    actions = ["make_available", "make_unavailable"]

    def make_available(self, request, queryset):
        updated = queryset.update(is_available=True)
        self.message_user(request, f"Marked {updated} bus(es) as available.")
    make_available.short_description = "Mark selected buses as available"

    def make_unavailable(self, request, queryset):
        updated = queryset.update(is_available=False)
        self.message_user(request, f"Marked {updated} bus(es) as unavailable.")
    make_unavailable.short_description = "Mark selected buses as unavailable"

@admin.register(Route)  
class RouteAdmin(admin.ModelAdmin):
    list_display = ["id", "route_name"]

@admin.register(BusSchedule)
class BusScheduleAdmin(admin.ModelAdmin):
    list_display = ["id", "bus"]

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(FleetSettings)
class FleetSettingsAdmin(admin.ModelAdmin):
    list_display = ["available_buses"]
    # Enforce singleton: prevent adding more than one FleetSettings row
    def has_add_permission(self, request):
        return not FleetSettings.objects.exists()
