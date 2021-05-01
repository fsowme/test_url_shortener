from django.urls import path

from shortener import views

urlpatterns = [
    path("<str:short_path>/", views.get_short_url),
    path("", views.make_short_url),
]
