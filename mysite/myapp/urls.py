from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/", views.greed, name="greed"),
    path("brian/", views.brian, name="brian"),
]
