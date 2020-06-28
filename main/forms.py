from .models import short_urls

from django import forms


class Url_form(forms.ModelForm):
    class Meta:
        model = short_urls
        fields = "__all__"
        exclude = ("short_url",)

