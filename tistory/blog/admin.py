from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Blog

# Register your models here.
admin.site.register(Blog)