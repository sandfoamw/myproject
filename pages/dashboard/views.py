from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_page
from django.template.response import TemplateResponse


menus = {
    'dashboard': 'DASHBOARD',
    'dashboard1': 'DASHBOARD V1',
    'dashboard2': 'DASHBOARD V2'
}


@require_GET
@cache_page(60 * 15, key_prefix='index1')
def Index(request):
    return TemplateResponse(request, 'dashboard/index.html', context=menus)


class Index2(TemplateView):
    template_name = 'dashboard/index2.html'