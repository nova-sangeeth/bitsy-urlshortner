from django.shortcuts import render, redirect
from .models import short_urls, UserProfile
from .forms import Url_form, profile_registration_form
from .shortner import shortner
from .url_ext import url_sep
import tldextract
from .custom_domain_slugs import *
from django.contrib.auth.models import User


def index(request):
    return render(request, "index.html")


def home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def profile(request):
    user = UserProfile.objects.filter(user=request.user)
    return render(request, "profile.html", {"user": user})


def registration(request):
    user = User.objects.get(username=request.user.username)
    profile = UserProfile(user=user)
    form = profile_registration_form(request.POST or None, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "registration.html", {"form": form})


def new_url(request):
    form = Url_form(request.POST)
    shortened_url = ""
    slug_seperator = "-"
    if request.method == "POST":
        if form.is_valid():
            new_url = form.save(commit=False)
            extracted_url = tldextract.extract(form.cleaned_data["long_url"])
            # code for checking the url for its domain
            if extracted_url.domain == "amazon":
                shortened_url = (
                    shortner().issue_token()
                    + slug_seperator
                    + amazon_slug
                    + new_url.slug
                )
            elif extracted_url.domain == "google":
                shortened_url = (
                    shortner().issue_token()
                    + slug_seperator
                    + google_slug
                    + new_url.slug
                )
            elif extracted_url.domain == "facebook":
                shortened_url = (
                    shortner().issue_token()
                    + slug_seperator
                    + facebook_slug
                    + new_url.slug
                )
            elif extracted_url.domain == "youtube":
                shortened_url = (
                    shortner().issue_token()
                    + slug_seperator
                    + youtube_slug
                    + new_url.slug
                )
            else:
                shortened_url = shortner().issue_token() + slug_seperator + new_url.slug
            # -------------------------------

            new_url.short_url = shortened_url
            new_url.save()
        else:
            form = Url_form()
            shortened_url = "Not a Valid URL."

    return render(
        request, "new_url.html", {"form": form, "shortened_url": shortened_url}
    )
