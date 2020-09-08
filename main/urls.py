from django.conf.urls import url
from .views import (
    index,
    new_url,
    profile,
    registration,
    home,
    edit_profile,
    my_url,
    new_url_anonymous,
    url_extract_info,
)

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^new_url/$", new_url, name="new_url"),
    url(r"^profile/$", profile, name="profile"),
    url(r"^registration/$", registration, name="registration"),
    url(r"^edit_profile/$", edit_profile, name="edit_profile"),
    url(r"^my_url/$", my_url, name="my_url"),
    url(r"^url_info/$", url_extract_info, name="url_extract_info"),
    url(r"^anonymous/$", new_url_anonymous, name="anonymous"),
]

