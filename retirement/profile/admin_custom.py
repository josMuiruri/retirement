from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "Retirement Community Adminstration"
    site_title = "Retirement Admin Portal"
    index_title = "Welcome to Retirement Community Admin"

admin_site = MyAdminSite(name='myadmin')