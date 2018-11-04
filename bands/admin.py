from django.contrib import admin

from .models import Artist, Venue, Event


class ArtistAdmin(admin.ModelAdmin):

    list_display = ['name', 'is_approved']
    fields = ['name', 'is_approved']
    list_filter = ['is_approved']


class VenueAdmin(admin.ModelAdmin):

    list_display = ['name', 'is_approved']
    fields = ['name', 'is_approved']
    list_filter = ['is_approved']


class EventAdmin(admin.ModelAdmin):

    list_display = ['title', 'date_and_time', 'is_approved']
    fields = ['title', 'date_and_time', 'is_approved']
    list_filter = ['is_approved']


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
