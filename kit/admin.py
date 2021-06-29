from django.contrib import admin
from .models import Surfboard, Wetsuit, Misc_Item

class SurfboardAdmin(admin.ModelAdmin):
    model = Surfboard
    list_display = ['IDnumber', 'brand', 'model', 'size', 'ability', 'location']

class WetsuitAdmin(admin.ModelAdmin):
    model = Wetsuit
    list_display = ['IDnumber', 'brand', 'model', 'thickness', 'size', 'location']

class MiscAdmin(admin.ModelAdmin):
    model = Misc_Item
    list_display = ['IDnumber', 'item_type', 'brand', 'location']

admin.site.register(Surfboard, SurfboardAdmin)
admin.site.register(Wetsuit, WetsuitAdmin)
admin.site.register(Misc_Item, MiscAdmin)
