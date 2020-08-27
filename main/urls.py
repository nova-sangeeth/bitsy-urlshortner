from django.conf.urls import url
from .views import index, new_url, about

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^about$", about, name="about"),
    url(r"^new_url/$", new_url, name="new_url"),
]

