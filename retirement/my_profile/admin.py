from django.contrib import admin

from .models import Profiles

admin.site.register(Profiles)
# changing the site header
admin.site.site_header = 'Retirement'