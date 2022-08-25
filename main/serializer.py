from rest_framework import serializers
from .models import Project, Talent


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'location', 'roles']


class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = '__all__'
        # exclude = ['id']
