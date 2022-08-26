# from . import views
from .views import CompanyRegistrationView, TalentRegistrationView  #ProjectViewSet,  TalentViewSet, TalentViews
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
app_name = 'main'
# from main.views import HomePageView
#
urlpatterns = [
    path('registration/company/', CompanyRegistrationView.as_view(), name='register-company'),
    path('registration/taent/', TalentRegistrationView.as_view(), name='register-talent'),

    # path('talents/', TalentViews.as_view()),
    # path('talents/<int:pk>/', views.TalentDetail.as_view()),
    # path('projects/', ProjectViewSet.as_view()),
    # path('', HomePageView.as_view(), name='home'),
    # path('add', views.add),
    # path('remove', views.remove),
    # path('', views.index),
    # path('post/', views.post),

    # path('snippets/', views.SnippetList.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
