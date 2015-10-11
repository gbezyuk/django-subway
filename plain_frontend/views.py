from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.template import loader


def home(request, template_name="plain_frontend/home.html"):
    return HttpResponse(loader.get_template(template_name).render(RequestContext(request, locals())))


def assignations(request, template_name="plain_frontend/assignations.html"):
    return HttpResponse(loader.get_template(template_name).render(RequestContext(request, locals())))


def developers(request, template_name="plain_frontend/developers.html"):
    return HttpResponse(loader.get_template(template_name).render(RequestContext(request, locals())))

def about(request, template_name="plain_frontend/about.html"):
    return HttpResponse(loader.get_template(template_name).render(RequestContext(request, locals())))
