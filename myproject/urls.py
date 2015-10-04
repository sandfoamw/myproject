"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.cache import cache_page
from pages.dashboard.views import Index1, Index2

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index1, name="INDEX"),
    url(r'^index2/$', cache_page(60 * 15, key_prefix='index2')(Index2.as_view()), name="INDEX2"),
]
