from .models import short_urls, UserProfile

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

