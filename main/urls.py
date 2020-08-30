from django.conf.urls import url
from .views import index, new_url, profile, registration, home, edit_profile

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^new_url/$", new_url, name="new_url"),
    url(r"^profile/$", profile, name="profile"),
    url(r"^registration/$", registration, name="registration"),
    url(r"^edit_profile/$", edit_profile, name="edit_profile"),
]

