from django.contrib import admin

from flights.models import Airport, Flight,Passenger

class Flightadmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, Flightadmin)
admin.site.register(Passenger)