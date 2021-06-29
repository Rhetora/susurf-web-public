from django.contrib import admin

from .models import BasePage, HomePage, CommitteePage, JoinPage, AboutPage, SpotsPage, spots
# Register your models here.
admin.site.register(BasePage)
admin.site.register(HomePage)
admin.site.register(CommitteePage)
admin.site.register(JoinPage)
admin.site.register(AboutPage)



admin.site.register(SpotsPage)

admin.site.register(spots)