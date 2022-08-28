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
from .serializer import ProjectSerializer, TalentRegistrationSerializer
# from .serializer import  ProjectSerializer, ApplicationSerializer # CompanySerializer, RoleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
# from result.models import Marksheet #application
"""
Index function is for the home page of the website.
"""
from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .serializer import CompanyRegistrationSerializer, TalentRegistrationSerializer, ApplicationSerializer
from rest_framework.decorators import api_view


class TalentViews(APIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']
    def get(self, request, format=None):
         talents = Talent.objects.all()
         serializer = TalentRegistrationSerializer(talents, many=True)
         return Response(serializer.data)

    def post(self, request):
        serializer = TalentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TalentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentRegistrationSerializer


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
        projects = Project.objects.all()  # filter(user = request.id)
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
            'location': request.data.get('location'),
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

    def get_object(self, project_name_id, company_name_id):
        '''
        Helper method to get the object with given project_name_id, and user_id
        '''
        try:
            return Project.objects.get(id=project_name_id, user=company_name_id)
        except Project.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, project_name_id, *args, **kwargs):
        '''
        Retrieves the project with given company_name_id
        '''
        todo_instance = self.get_object(project_name_id, request.company_name_id)
        if not todo_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProjectSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, project_name_id, *args, **kwargs):
        '''
        Updates the project item with given id if exists
        '''
        project_instance = self.get_object(project_name_id, request.company_name.id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exists"},
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
        serializer = ProjectSerializer(instance=project_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, project_name_id, *args, **kwargs):
        '''
        Deletes the project item with given id if exists
        '''
        project_instance = self.get_object(project_name_id, request.user.id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exists"},
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

    def get(self, request, pk=None):
        if pk:
            application = get_object_or_404(Application.objects.all(), pk=pk)
            serializer = ApplicationSerializer(application)
            return Response({"application": serializer.data})
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response({"applications": serializer.data})

    def post(self, request):
        application = request.data.get('application')

        # Create an application from the above data
        serializer = ApplicationSerializer(data=application)
        if serializer.is_valid(raise_exception=True):
            application_saved = serializer.save()
        return Response({"success": "application '{}' created successfully".format(application_saved.title)})

    def put(self, request, pk):
        saved_application = get_object_or_404(Application.objects.all(), pk=pk)
        data = request.data.get('application')
        serializer = ApplicationSerializer(instance=saved_application, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            application_saved = serializer.save()
        return Response({"success": "application '{}' updated successfully".format(application_saved.title)})

    def delete(self, request, pk):
        # Get object with this pk
        application = get_object_or_404(Application.objects.all(), pk=pk)
        application.delete()
        return Response({"message": "application with id `{}` has been deleted.".format(pk)}, status=204)

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
