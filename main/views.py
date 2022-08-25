from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.template.context_processors import csrf
from django.shortcuts import redirect, render
# from .models import Task
from django.http import HttpResponse
from django.template import loader
# from django.urls import

# Create your views here.

#
# def index(request):
#     template = loader.get_template('index.html')
#     tasks = Task.objects.order_by("id")
#     more_tasks = Task.objects.filter()
#     context = {'tasks': tasks}
#     context.update(csrf(request))
#     # return render('index.html', context)
#     return HttpResponse(template.render(context, request))
#
#
# def add(request):
#     item = Task(name=request.POST["name"])
#     item.save()
#     return redirect("/")
#
#
# def remove(request):
#     item = Task.objects.get(id=request.POST["id"])
#     if item:
#         item.delete()
#     return redirect("/")
#
#
# def post(request):
#     template = loader.get_template('index.html')
#     mabasa = Task.objects.all()
#     context = {'mabase': mabasa}
#     return HttpResponse(template.render(context, request))
