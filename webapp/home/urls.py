"""URLS for static pages."""

from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name="home_index"),
    path('about', views.about, name="home_about"),
    path('landing', views.landing, name="home_landing"),
    path('request', views.user_request, name="user_request"),
    path('request/tool', views.user_request_tool, name="user_request_tool"),
    path('request/quota', views.user_request_quota, name="user_request_quota"),
    path('request/support',
         views.user_request_support, name="user_request_support"),
    path('aaf-institutions', views.aaf_institutions,
         name="home_aaf_institutions"),
    re_path(r'^[\w\d\_-]+.html$', views.page, name='home_page'),
]
