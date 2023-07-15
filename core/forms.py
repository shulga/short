from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(required=True, max_length=255)
    hashed_url = forms.CharField(required=False, min_length=3, max_length=10)
