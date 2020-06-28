from django.shortcuts import render, redirect
from .models import short_urls
from .forms import Url_form
from .shortner import shortner


def index(request):
    return render(request, "index.html")


def home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def new_url(request):
    form = Url_form(request.POST)
    a = ""
    if request.method == "POST":
        if form.is_valid():
            new_url = form.save(commit=False)
            a = shortner().issue_token()
            new_url.short_url = a
            new_url.save()
        else:
            form = Url_form()
            a = "Not a Valid URL "

    return render(request, "new_url.html", {"form": form, "a": a})
