from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members


# Create your views here.
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def members(request):
    my_members = Members.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {"my_members": my_members}
    return HttpResponse(template.render(context, request))


def details(request, id):
    my_member = Members.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {"my_member": my_member}
    return HttpResponse(template.render(context, request))


def testing(request):
    my_members = Members.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        "my_members": my_members,
    }
    return HttpResponse(template.render(context, request))
