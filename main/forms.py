from .models import short_urls, UserProfile, user_created_url

from django import forms


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


class user_url_form(forms.ModelForm):
    class Meta:
        model = user_created_url
        fields = "__all__"
        exclude = ("user",)
