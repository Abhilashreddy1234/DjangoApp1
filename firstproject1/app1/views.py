from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import member
def app1(request):
    mymembers=member.objects.all().values()
    template=loader.get_template('file2.html')
    context={
        'mymembers':mymembers,    
        }
    return HttpResponse(template.render(context,request))
def details(request,id):
    mymembers=member.objects.get(id=id)
    template=loader.get_template('file3.html')
    context={
        'mymembers':mymembers, 
    }
    return HttpResponse(template.render(context,request))
def main(request):
    template=loader.get_template('main.html')
    context={
     'mymembers':member,   
    }
    return HttpResponse(template.render(context,request))
