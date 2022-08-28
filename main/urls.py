# from . import views
from . import views
from .views import ApplicationView, ProjectsView #ProjectViewSet,  TalentViewSet, TalentViews, CompanyRegistrationView, TalentRegistrationView
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path
from django.template.defaulttags import url
app_name = 'main'
# from main.views import HomePageView
#
urlpatterns = [
    # # url(r'^comregview$', views.comregview),
    # path('comreg/', views.comregview),
    # path('registration/company/', CompanyRegistrationView.as_view(), name='register-company'),
    # path('registration/talent/', TalentRegistrationView.as_view(), name='register-talent'),
    # http://127.0.0.1:8000/accounts/register/register/
    # path('talents/', TalentViews.as_view()),
    path('application/', ApplicationView.as_view()),
    # path('talents/<int:pk>/', views.TalentDetail.as_view()),
    path('projects/', ProjectsView.as_view()),
    # path('', HomePageView.as_view(), name='home'),
    # path('add', views.add),
    # path('remove', views.remove),
    # path('', views.index),
    # path('post/', views.post),

    # path('snippets/', views.SnippetList.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
