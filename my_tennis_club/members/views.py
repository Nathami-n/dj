
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member


def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    
    context = {
        "mymembers": my_members,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    template  = loader.get_template("home.html")
    return render(request, "home.html")


def details(request, id):
    mymember = Member.objects.get(id=id)
    return render(request, "details.html", {"mymember": mymember})