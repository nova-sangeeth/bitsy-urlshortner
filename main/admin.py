from django.contrib import admin

# Register your models here.
from .models import short_urls

admin.site.register(short_urls)
