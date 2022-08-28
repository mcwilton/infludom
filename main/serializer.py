from rest_framework import serializers
from .models import Project, Talent, Company, Application, Role
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class CompanyRegistrationSerializer(RegisterSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    area = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(CompanyRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'area': self.validated_data.get('area', ''),
            'address': self.validated_data.get('address', ''),
            'description': self.validated_data.get('description', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(CompanyRegistrationSerializer, self).save(request)
        user.is_company = True
        user.save()
        company = Company(company=user, area=self.cleaned_data.get('area'),
                        address=self.cleaned_data.get('address'),
                        description=self.cleaned_data.get('description'))
        company.save()
        return user


class TalentRegistrationSerializer(RegisterSerializer):
    talent = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    country = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(TalentRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'country': self.validated_data.get('country', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(TalentRegistrationSerializer, self).save(request)
        user.is_buyer = True
        user.save()
        talent = Talent(talent=user, country=self.cleaned_data.get('country'))
        talent.save()
        return user



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['project_name', 'description', 'location', 'roles']


# class TalentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Talent
#         fields = '__all__'


# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = '__all__'



