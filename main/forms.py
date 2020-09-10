from .models import short_urls, UserProfile, user_created_url

from django import forms
from django.contrib.auth import get_user_model


class Url_form(forms.ModelForm):
    class Meta:
        model = short_urls
        fields = "__all__"
        exclude = ("short_url",)


class profile_registration_form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ("user",)


class custom_allauth_registration_form(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    # Gender = forms.CharField(max_length=6)

    class Meta:
        model = get_user_model

    def save(self, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()


class user_url_form(forms.ModelForm):
    class Meta:
        model = user_created_url
        fields = "__all__"
        exclude = ("user", "short_url")


class url_info_form(forms.Form):
    URL = forms.URLField(max_length=512, label="Enter the URL")
