from django.contrib import admin
from .models import Event, beginnerSignupEntry, weekendSignupEntry

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['name', 'event_type']
    fieldsets = (
        ('General', {
            'fields': ('name', 'event_type', 'location', 'shortDescription', 'longDescription', 'cost')
        }),
        ('Times', {
            'fields': ('startDateTime', 'endDateTime', 'publishDateTime'),
        }),
        ('If a signup is needed', {
            'classes': ('collapse',),
            'fields': ('signupRequired', 'signupPublish', 'signupClose', 'spaces', 'endQuestion'),
        }),
        ('For Weekend Trips', {
            'classes': ('collapse',),
            'fields': ('camping',),
        }),
        ('For Abroad Trips', {
            'classes': ('collapse',),
            'fields': ('rentalAvailable', 'lessonsAvailable'),
        })

    )

admin.site.register(Event, EventAdmin)
admin.site.register(weekendSignupEntry)
