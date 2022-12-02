from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MySpaceViews(LoginRequiredMixin, TemplateView):
    template_name = "base/myspace.html"


def page_not_found_view(request, exception):
    template_name = 'error/404.html'
    return render(request, template_name, status='404')


def error_view(request):
    template_name = 'error/500.html'
    return render(request, template_name, status='500')


def permission_denied_view(request, exception):
    template_name = 'error/403.html'
    return render(request, template_name, status='403')


def bad_request_view(request, exception):
    template_name = 'error/400.html'
    return render(request, template_name, status='400')
