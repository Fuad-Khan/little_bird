from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('service', 'user', 'date', 'time', 'is_confirmed')
    list_filter = ('service', 'is_confirmed', 'date')
    search_fields = ('user__username', 'service__title', 'phone')
