from django.shortcuts import render, redirect
from .models import short_urls
from .forms import Url_form
from .shortner import shortner
from .url_ext import url_sep


def index(request):
    return render(request, "index.html")


def home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def new_url(request):
    form = Url_form(request.POST)
    shortened_url = ""
    slug_seperator = "-"
    if request.method == "POST":
        if form.is_valid():
            new_url = form.save(commit=False)
            # shortened_url = shortner().issue_token() + slug_seperator + new_url.slug
            shortened_url = url_sep().issue_token() + slug_seperator + new_url.slug
            new_url.short_url = shortened_url
            new_url.save()
        else:
            form = Url_form()
            shortened_url = "Not a Valid URL."

    return render(
        request, "new_url.html", {"form": form, "shortened_url": shortened_url}
    )
