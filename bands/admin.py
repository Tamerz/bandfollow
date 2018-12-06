from django.contrib import admin

from .models import User, Artist, Venue, Event, Alert
from import_export import resources
from import_export.admin import ImportExportModelAdmin


def approve_artist(modeladmin, request, queryset):
    for artist in queryset:
        artist.is_approved = True
        artist.save()
    approve_artist.short_description = 'Approve selected artists'


def approve_venue(modeladmin, request, queryset):
    for venue in queryset:
        venue.is_approved = True
        venue.save()
    approve_venue.short_description = 'Approve selected venues'


def approve_event(modeladmin, request, queryset):
    for event in queryset:
        event.is_approved = True
        event.save()
    approve_event.short_description = 'Approve selected events'


class ArtistResource(resources.ModelResource):
    class Meta:
        model = Artist


class VenueResource(resources.ModelResource):
    class Meta:
        model = Venue


class EventResource(resources.ModelResource):
    class Meta:
        model = Event


class ArtistAdmin(ImportExportModelAdmin):

    list_display = ['name', 'website', 'is_approved']
    actions = [approve_artist, ]
    fields = ['name', 'website', 'is_approved']
    list_filter = ['is_approved']
    resource_class = ArtistResource


class VenueAdmin(ImportExportModelAdmin):

    list_display = ['name', 'website', 'is_approved']
    actions = [approve_venue, ]
    fields = ['name', 'website', 'is_approved']
    list_filter = ['is_approved']
    resource_class = VenueResource


class EventAdmin(ImportExportModelAdmin):

    list_display = ['title', 'date_and_time', 'is_approved', 'venue', 'artist_list']
    actions = [approve_event, ]
    fields = ['title', 'date_and_time', 'is_approved', 'venue', 'artists']
    list_filter = ['is_approved']
    resource_class = EventResource


admin.site.register(User)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Alert)
