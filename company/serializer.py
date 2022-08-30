from rest_framework import serializers
from company.models import Project, Application, Company, Role


class ProjectSerializer(serializers.Serializer):
    company_name = serializers.CharField(required =True)
    project_name = serializers.CharField(required =True)
    description = serializers.CharField(max_length=200)
    location = serializers.CharField(required=True)
    ethnicity = serializers.CharField(required=True)
    role_name = serializers.CharField(required=True)


    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.ethnicity = validated_data.get('ethnicity', instance.ethnicity)
        instance.role_name = validated_data.get('role_name', instance.role_name)
        instance.save()
        return instance


class RoleSerializer(serializers.Serializer):
    role_name = serializers.CharField(required =True)
    email = serializers.EmailField()
    talent_gender = serializers.CharField(max_length=200)
    talent_ethnicity = serializers.CharField(required=True)
    talent_weight = serializers.DecimalField(required=True, max_digits=4, decimal_places=2)
    talent_height = serializers.DecimalField(required=True,  max_digits=4, decimal_places=2)

    def create(self, validated_data):
        return Role.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.role_name = validated_data.get('role_name', instance.role_name)
        instance.email = validated_data.get('email', instance.email)
        instance.talent_gender = validated_data.get('talent_gender', instance.talent_gender)
        instance.talent_ethnicity = validated_data.get('talent_ethnicity', instance.talent_ethnicity)
        instance.talent_weight = validated_data.get('talent_weight', instance.talent_weight)
        instance.talent_height = validated_data.get('talent_height', instance.talent_height)
        instance.save()
        return instance


class ApplicationSerializer(serializers.Serializer):
    role_name = serializers.CharField(required =True)
    applicant_name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Application.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.role_name = validated_data.get('role_name', instance.role_name)
        instance.applicant_name = validated_data.get('applicant_name', instance.applicant_name)
        instance.save()
        return instance


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
