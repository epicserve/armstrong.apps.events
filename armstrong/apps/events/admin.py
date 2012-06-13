from django.contrib import admin
from .models import Event, RSVP


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Event, EventAdmin)
admin.site.register(RSVP)
