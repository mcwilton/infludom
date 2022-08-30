from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path
from django.template.defaulttags import url
from .views import ApplicationView, ProjectsView, ProjectDetailApiView, RoleDetailApiView, RoleView,  CompanyRegistrationView

app_name = 'company'


urlpatterns = [
    path('projects/', ProjectsView.as_view(), name ='ProjectsView'),
    path('projects/<int:project_id>/', ProjectDetailApiView.as_view()),
    path('applications/', ApplicationView.as_view()),
    path('applications/<int:pk>', ApplicationView.as_view()),
    path('registration/', CompanyRegistrationView.as_view()),
    path('roles/', RoleView.as_view(), name ='RoleView'),
    path('roles/<int:role_name_id>/', RoleDetailApiView.as_view()),

]