from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import permissions
from django.template.context_processors import csrf
from django.shortcuts import redirect, render
from .models import Talent
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializer import TalentRegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view


class TalentViews(APIView):
    # permission_classes = (permissions.AllowAny,)
    # http_method_names = ['get', 'head']
    def get(self, request,  format=None):
         talents = Talent.objects.all()
         serializer = TalentRegistrationSerializer(talents, many=True)
         return Response(serializer.data)

    def post(self, request):
        serializer = TalentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TalentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentRegistrationSerializer

class TalentRegistrationView(APIView):
    serializer_class = TalentRegistrationSerializer


def index(request):
    template = loader.get_template('index.html')
    # tasks = Task.objects.order_by("id")
    # more_tasks = Task.objects.filter()
    context = {'tasks': "welcome"}
    context.update(csrf(request))
    # return render('index.html', context)
    return HttpResponse(template.render(context, request))


    # def get(self, request, *args, **kwargs):
    #     applications = Application.objects.all()
    #     serializer = ApplicationSerializer(applications, many=True)
    #     return Response({"applications": serializer.data})
    #
    # def post(self, request, *args, **kwargs):
    #     application = request.data.get('application')
    #
    #     serializer = ApplicationSerializer(data=application)
    #     if serializer.is_valid(raise_exception=True):
    #         application_saved = serializer.save()
    #     return Response({"success": "Application '{}' created successfully".format(application)})


    # permission_classes = (permissions.AllowAny,)
    # http_method_names = ['get', 'head']
    #
    # queryset = Group.objects.all()
    # serializer_class = ApplicationSerializer