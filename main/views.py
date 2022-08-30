from rest_framework.generics import get_object_or_404

from .models import Talent
from rest_framework import viewsets, generics
from .serializer import TalentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TalentRegistrationView(APIView):
    serializer_class = TalentSerializer


class TalentViews(APIView):

    def get(self, request, format=None):
        talents = Talent.objects.all()
        serializer = TalentSerializer(talents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        talents = request.data.get('talents'),

        # 'username': request.data.get('username'),
        # 'bio': request.data.get('bio'),
        # 'phone_number': request.data.get('phone_number'),
        # 'gender': request.data.get('gender'),
        # 'age': request.data.get('age'),
        # 'weight': request.data.get('weight'),
        # 'height': request.data.get('height'),
        # 'email': request.data.get('email'),

        serializer = TalentSerializer(data=talents)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        saved_talent = get_object_or_404(Talent.objects.all(), pk=pk)
        data = request.data.get('application')
        serializer = TalentSerializer(instance=saved_talent, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        # Get object with this pk
        talent = get_object_or_404(Talent.objects.all(), pk=pk)
        talent.delete()
        return Response(talent.data, status=status.HTTP_204_NO_CONTENT)


class TalentDetailView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, talent_name_id):
        '''
        Helper method to get the object with given project_name_id, and user_id
        '''
        try:
            return Talent.objects.get(id=talent_name_id)
        except Talent.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, talent_name_id, *args, **kwargs):
        '''
        Retrieves the Talent with given company_name_id
        '''
        talent_instance = self.get_object(talent_name_id)
        if not talent_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TalentSerializer(talent_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, talent_name_id, *args, **kwargs):
        '''
        Updates the Talent item with given id if exists
        '''
        talent_instance = self.get_object(talent_name_id)
        if not talent_instance:
            return Response(
                {"res": "Object with instance id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'username': request.data.get('username'),
            'bio': request.data.get('bio'),
            'phone_number': request.data.get('phone_number'),
            'gender': request.data.get('gender'),
            'age': request.data.get('age'),
            'weight': request.data.get('weight'),
            'height': request.data.get('height'),
            'email': request.data.get('email'),
            # 'user': request.user.id

        }
        serializer = TalentSerializer(instance=talent_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, talent_name_id, *args, **kwargs):
        '''
        Deletes the Talent item with given id if exists
        '''
        talent_instance = self.get_object(talent_name_id)
        if not talent_instance:
            return Response(
                {"res": "Object with talent id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        talent_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
