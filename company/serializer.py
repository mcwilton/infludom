from rest_framework import serializers
from company.models import Project, Application, Company, Role


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['company_name','project_name', 'description', 'location', 'ethnicity', 'role_name']


class RoleSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Application.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.applicant_name = validated_data.get('title', instance.title)
        instance.role = validated_data.get('description', instance.description)
        instance.save()
        return instance
    class Meta:
        model = Role
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Application.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.applicant_name = validated_data.get('title', instance.title)
        instance.role = validated_data.get('description', instance.description)
        instance.save()
        return instance

    class Meta:
        model = Application
        fields = ['applicant_name', 'role']


class CompanyRegistrationSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(required=True)  # by default allow_null = False
    email = serializers.EmailField(required=True)
    description = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(CompanyRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'company_name': self.validated_data.get('company_name', ''),
            'email': self.validated_data.get('email', ''),
            'description': self.validated_data.get('description', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(CompanyRegistrationSerializer, self).save(request)
        user.is_company = True
        user.save()
        company = Company(company=user, company_name=self.cleaned_data.get('area'),
                          email=self.cleaned_data.get('email'),
                          description=self.cleaned_data.get('description'))
        company.save()
        return user
