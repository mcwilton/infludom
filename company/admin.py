from django.contrib import admin
from .models import Project, Company, Ethnicity, Role, Application, Ethnicity

@admin.register(Application)
class Application(admin.ModelAdmin):
    list_display = ('applicant_name', 'role')
    list_filter = ('applicant_name', 'role')
    search_fields = ('applicant_name', 'role')


@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'description', 'created_at', 'updated_at')
    list_filter = ('company_name', 'email')
    search_fields = ('company_name', 'email')


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ('project_name', 'description', 'location', 'role_name')
    list_filter = ('location', 'role_name')
    search_fields = ('location', 'role_name')


@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display = ('role_name', 'talent_age', 'talent_gender', 'talent_ethnicity', 'talent_weight', 'talent_height')
    list_filter = ('talent_age', 'talent_gender', 'talent_ethnicity')
    search_fields = ('talent_age', 'talent_gender', 'talent_ethnicity')


@admin.register(Ethnicity)
class Ethnicity(admin.ModelAdmin):
    list_display = ('ethnicity',)
    list_filter = ('ethnicity',)
    search_fields = ('ethnicity',)