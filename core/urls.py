from django.urls import path

from .views import HomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home_page"),
    path("<str:code>", HomeView.go, name="home_page"),
]
