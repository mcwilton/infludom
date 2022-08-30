from .views import  TalentRegistrationView, TalentDetailView, TalentViews
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path, reverse, reverse_lazy
from django.template.defaulttags import url


app_name = 'main'
found = reverse_lazy('TalentViews')


urlpatterns = [

    path('talent/', TalentViews.as_view(), name='TalentViews'),
    path('talent/<int:pk>/', TalentDetailView.as_view()),
    path('registration/talent/', TalentRegistrationView.as_view()),

    # http://127.0.0.1:8000/accounts/register/register/

]
urlpatterns = format_suffix_patterns(urlpatterns)
