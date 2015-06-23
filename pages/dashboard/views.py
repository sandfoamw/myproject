from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'dashboard/index.html'


class Index2(TemplateView):
    template_name = 'dashboard/index2.html'