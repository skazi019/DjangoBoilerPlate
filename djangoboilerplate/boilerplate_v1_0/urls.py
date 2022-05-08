# from django.conf.urls import url
from boilerplate_v1_0.views import home, register
from django.urls import re_path, include


urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^home/", home, name="home"),
    re_path(r"^register/", register, name="register"),
]
