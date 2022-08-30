from .models import Project, Company, Application, Role
from .serializer import ProjectSerializer, CompanyRegistrationSerializer, ApplicationSerializer, RoleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class CompanyRegistrationView(APIView):
    # serializer_class = CompanyRegistrationSerializer
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all companies
    def get(self, request, *args, **kwargs):
        '''
        List all the items for given requested user
        '''
        companies = Company.objects.all()  # filter(user = request.id)
        serializer = CompanyRegistrationSerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Company
        '''
        data = {

            'company_name': request.data.get('company_name'),
            'description': request.data.get('description'),
            'email': request.data.get('email'),
            # 'user': request.user.id
        }
        serializer = CompanyRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectsView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all projects
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
    # permission_classes = [permissions.IsAuthenticated]

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
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        application = request.data.get('application')

        # Create an application from the above data
        serializer = ApplicationSerializer(data=application)
        if serializer.is_valid(raise_exception=True):
            application_saved = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        saved_application = get_object_or_404(Application.objects.all(), pk=pk)
        data = request.data.get('application')
        serializer = ApplicationSerializer(instance=saved_application, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            application_saved = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        # Get object with this pk
        application = get_object_or_404(Application.objects.all(), pk=pk)
        application.delete()
        return Response(application.data, status=status.HTTP_204_NO_CONTENT)


class RoleView(APIView):
    # serializer_class = RoleSerializer
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all roles
    def get(self, request, *args, **kwargs):
        '''
        List all the items for given requested user
        '''
        roles = Role.objects.all()  # filter(user = request.id)
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create role
        '''
        data = {

            'role_name': request.data.get('role_name'),
            'talent_age': request.data.get('talent_age'),
            'talent_gender': request.data.get('talent_gender'),
            'talent_ethnicity': request.data.get('talent_ethnicity'),
            'talent_weight': request.data.get('talent_weight'),
            'talent_height': request.data.get('talent_height'),

        }
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, role_name_id, company_name_id):
        '''
        Helper method to get the object with given project_name_id, and user_id
        '''
        try:
            return Role.objects.get(id=role_name_id, user=company_name_id)
        except Role.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, role_name_id, *args, **kwargs):
        '''
        Retrieves the project with given company_name_id
        '''
        role_instance = self.get_object(role_name_id)
        if not role_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RoleSerializer(role_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, role_name_id, *args, **kwargs):
        '''
        Updates the project item with given id if exists
        '''
        role_instance = self.get_object(role_name_id, request.company_name.id)
        if not role_instance:
            return Response(
                {"res": "Object with instance id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'role_name': request.data.get('role_name'),
            'talent_age': request.data.get('talent_age'),
            'talent_gender': request.data.get('talent_gender'),
            'talent_ethnicity': request.data.get('talent_ethnicity'),
            'talent_weight': request.data.get('talent_weight'),
            'talent_height': request.data.get('talent_height'),
            # 'user': request.user.id
        }
        serializer = RoleSerializer(instance=role_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, role_name_id, *args, **kwargs):
        '''
        Deletes the project item with given id if exists
        '''
        role_instance = self.get_object(role_name_id, request.user.id)
        if not role_instance:
            return Response(
                {"res": "Object with role id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        role_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
