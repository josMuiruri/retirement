from django.contrib import admin
from .admin_custom import admin_site
from .models import Profiles


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

admin.site.register(Profiles, ProfileAdmin)