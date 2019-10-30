from django.urls import path
from troupes import views

urlpatterns = [
    path("", views.home, name="troupes-home"),
    path("about/", views.about, name="troupes-about"),
]
