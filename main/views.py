from django.http import Http404
from rest_framework.generics import get_object_or_404

from .models import Talent
from rest_framework import viewsets, generics
from .serializer import TalentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TalentRegistrationView(APIView):
    serializer_class = TalentSerializer


class TalentView(APIView):
    def get(self, request, format=None):
        talents = Talent.objects.all()
        serializer = TalentSerializer(talents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TalentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TalentDetail(APIView):

    def get_object(self, pk):
        try:
            return Talent.objects.get(pk=pk)
        except Talent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        talent = self.get_object(pk)
        serializer = TalentSerializer(talent)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        talent = self.get_object(pk)
        serializer = TalentSerializer(talent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        talent = self.get_object(pk)
        talent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


