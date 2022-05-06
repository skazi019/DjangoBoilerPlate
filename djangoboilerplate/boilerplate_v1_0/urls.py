# from django.conf.urls import url
from boilerplate_v1_0.views import dashboard, register
from django.urls import re_path, include


urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^register/", register, name="register")
]
