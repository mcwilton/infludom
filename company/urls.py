from django.urls import path
from .views import ApplicationView, ApplicationDetail, ProjectView, ProjectsDetail, RoleDetail, RoleView,  CompaniesView, CompanyDetail

app_name = 'company'


urlpatterns = [
    path('projects/', ProjectView.as_view(), name ='ProjectsView'),
    path('projects/<int:project_id>/', ProjectsDetail.as_view()),
    path('applications/', ApplicationView.as_view()),
    path('applications/<int:pk>', ApplicationDetail.as_view()),
    path('registration/', CompaniesView.as_view()),
    path('registration/<int:pk>', CompanyDetail.as_view()),
    path('roles/', RoleView.as_view(), name ='RoleView'),
    path('roles/<int:role_name_id>/', RoleDetail.as_view()),

]