from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.cache import cache_page

from core.models import Url
from core.forms import UrlForm
from django.shortcuts import get_object_or_404

class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})

        url = form.cleaned_data.get("url")
        hashed_url = form.cleaned_data.get("hashed_url")

        try:
            obj = Url.objects.create(url=url, hashed_url=hashed_url)
        except IntegrityError:
            form.add_error("hashed_url", "You can't use this shortcode")
            return render(request, self.template_name, {"form": form})



        return render(
            request, self.template_name, {"short_url": obj.get_full_short_url()}
        )

    """ 
        Get url by hash code and permanently redirect to the full url
        Cache for 5 mins as an example (invalidation needed for updated URLs)
    """
    @cache_page(60*5)
    def go(self, code):
        url = get_object_or_404(Url, hashed_url=code)
        return redirect(url.url, 302)