from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost
from .models import mycar

def mainpage(request):
  mymembers = BlogPost.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = BlogPost.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def mycar_list(request):
  mycars = mycar.objects.all()
  template = loader.get_template('mycar.html')
  data = {
    'mycar': mycars,
  }
  return HttpResponse(template.render(data, request))



