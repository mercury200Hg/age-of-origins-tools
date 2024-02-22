from django.urls import path

from . import views

app_name = "troops_calculator"
urlpatterns = [
    path("", views.index, name="index"),
]
