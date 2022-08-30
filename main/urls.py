from .views import  TalentRegistrationView, TalentDetail, TalentView
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


app_name = 'main'
# found = reverse_lazy('TalentViews')


urlpatterns = [

    path('talent/', TalentView.as_view(), name='TalentViews'),
    path('talent/<int:pk>/', TalentDetail.as_view()),
    path('registration/', TalentRegistrationView.as_view()),

    # http://127.0.0.1:8000/accounts/register/register/

]
urlpatterns = format_suffix_patterns(urlpatterns)
