from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, user_created_url, short_urls
from .forms import profile_registration_form, user_url_form, Url_form
from .shortner import shortner
import tldextract
from .custom_domain_slugs import *
from django.contrib.auth.models import User


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def home(request, token):
    current_user = request.user
    if current_user.is_authenticated:
        long_url = user_created_url.objects.filter(short_url=token)[0]
    else:
        long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def profile(request):
    current_user = UserProfile.objects.filter(user=request.user)
    return render(request, "user_profile.html", {"current_user": current_user})


def my_url(request):
    current_user = request.user
    my_url = user_created_url.objects.filter(user=current_user)
    count = user_created_url.objects.filter(user=current_user).count()

    return render(
        request,
        "my_urls.html",
        {"current_user": current_user, "my_url": my_url, "count": count},
    )


def registration(request):
    user = User.objects.get(username=request.user.username)
    profile = UserProfile(user=user)
    form = profile_registration_form(request.POST or None, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile")
    return render(request, "registration.html", {"form": form})


def edit_profile(request):
    user = User.objects.get(username=request.user.username)
    profile = get_object_or_404(UserProfile, user=user)
    form = profile_registration_form(request.POST or None, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile")
    return render(request, "edit_profile.html", {"form": form})


def new_url(request):
    form = user_url_form(request.POST)
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
            elif extracted_url.domain == "instagram":
                shortened_url = (
                    shortner().issue_token()
                    + slug_seperator
                    + instagram_slug
                    + new_url.slug
                )
            else:
                shortened_url = shortner().issue_token() + slug_seperator + new_url.slug
            # -------------------------------
            # added this line to link the user foreign key of the user
            new_url.user = request.user
            new_url.short_url = shortened_url
            new_url.save()
        else:
            form = Url_form()
            shortened_url = "Not a Valid URL."

    return render(
        request, "new_url.html", {"form": form, "shortened_url": shortened_url}
    )


def new_url_anonymous(request):
    form = Url_form(request.POST)
    shortened_url = ""
    slug_seperator = "-"
    if request.method == "POST":
        if form.is_valid():
            new_url = form.save(commit=False)

            shortened_url = shortner().issue_token() + slug_seperator
            # -------------------------------
            # added this line to link the user foreign key of the user
            new_url.short_url = shortened_url
            new_url.save()
        else:
            form = Url_form()
            shortened_url = "Not a Valid URL."

    return render(
        request,
        "new_url_anonymous.html",
        {"form": form, "shortened_url": shortened_url},
    )
