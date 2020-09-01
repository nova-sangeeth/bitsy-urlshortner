from django.contrib import admin

# Register your models here.
from .models import short_urls, UserProfile, user_created_url

admin.site.register(short_urls)
admin.site.register(UserProfile)
admin.site.register(user_created_url)
