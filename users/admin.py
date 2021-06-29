from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _

class UserAdmin(DefaultUserAdmin):
    model = CustomUser
    ordering = ('email',)
    search_fields = ('email',)
    list_display = ['email', 'first_name', 'last_name', 'member_type', 'is_active', 'date_joined']
    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name'), 'email', 'member_type', 'is_active', 'is_staff')
        }),
        ('Personal Info', {
            'fields': ('student_id', 'dob', 'dietary', 'medical', 'phone', 'bio'),
        }),
        ('Next of Kin', {
            'classes': ('collapse',),
            'fields': ('kin_name', 'kin_relation', 'kin_number', 'kin_address1', 'kin_address2', 'kin_address3', 'kin_postcode'),
        }),
        ('Information', {
            'classes': ('collapse',),
            'fields': ('ability', 'wetsuit', 'large_board', 'short_board', 'car', 'car_seats', 'minibus', 'swim100m', 'paid'),
        }),
        ('Admin Settings', {
            'classes': ('collapse',),
            'fields': ('is_superuser', 'last_login', 'date_joined'),
        })

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, UserAdmin)
