from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import permissions
from django.template.context_processors import csrf
from django.shortcuts import redirect, render
from .models import Talent, Project, Company, Application, Role
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializer import ProjectSerializer
# from .serializer import  ProjectSerializer, ApplicationSerializer # CompanySerializer, RoleSerializerTalentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# from result.models import Marksheet #application
"""
Index function is for the home page of the website.
"""
from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .serializer import CompanyRegistrationSerializer, TalentRegistrationSerializer, ApplicationSerializer
from rest_framework.decorators import api_view

#
# @api_view(['GET', 'POST', 'DELETE'])
# class CompanyRegistrationView(RegisterView):
#     serializer_class = CompanyRegistrationSerializer
#
#
# @api_view(['GET', 'POST', 'DELETE'])
# class TalentRegistrationView(RegisterView):
#     serializer_class = TalentRegistrationSerializer


class ProjectsView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the items for given requested user
        '''
        projects = Project.objects.all() #filter(user = request.id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Project
        '''
        data = {
            'project_name': request.data.get('project_name'),
            'company_name': request.data.get('company_name'),
            'description': request.data.get('description'),
            'location' : request.data.get('location'),
            'ethnicity': request.data.get('ethnicity'),
            'role_name': request.data.get('role_name'),
              # 'user': request.user.id
        }
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, todo_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Project.objects.get(id=todo_id, user = user_id)
        except Project.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, todo_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProjectSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, todo_id, *args, **kwargs):
        '''
        Updates the project item with given id if exists
        '''
        project_instance = self.get_object(todo_id, request.user.id)
        if not project_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'project_name': request.data.get('project_name'),
            'company_name': request.data.get('company_name'),
            'description': request.data.get('description'),
            'location': request.data.get('location'),
            'ethnicity': request.data.get('ethnicity'),
            'role_name': request.data.get('role_name'),
            # 'user': request.user.id
        }
        serializer = ProjectSerializer(instance = project_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        '''
        Deletes the project item with given id if exists
        '''
        project_instance = self.get_object(todo_id, request.user.id)
        if not project_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        project_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

# company views
# @login_required
# def marksheet_list(request):
#     profile = Profile.objects.filter(user_id=request.user.id).first()  #company profile
#     marksheets = Marksheet.objects.filter(student_name=profile)
#     return render(request, 'result/marksheet_list.html', {'marksheets': marksheets})
#
#
# class MarksheetDetailView(LoginRequiredMixin, DetailView):
#     model = Marksheet


# class TalentViews(APIView):
#     def post(self, request):
#         serializer = TalentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class TalentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Talent.objects.all()
#     serializer_class = TalentSerializer
#

def index(request):
    template = loader.get_template('index.html')
    # tasks = Task.objects.order_by("id")
    # more_tasks = Task.objects.filter()
    context = {'tasks': "welcome"}
    context.update(csrf(request))
    # return render('index.html', context)
    return HttpResponse(template.render(context, request))


class ApplicationView(APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = ApplicationSerializer



# class TalentViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = TalentSerializer


# class ProjectViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = ProjectSerializer

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
