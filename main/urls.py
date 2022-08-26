from . import views
from .views import TalentViewSet, ProjectViewSet, TalentViews

from django.urls import path

# from main.views import HomePageView
#
urlpatterns = [
    path('talents/', TalentViews.as_view()),
    # path('ProjectViewSet/', ProjectViewSet.as_view()),
    # path('', HomePageView.as_view(), name='home'),
    # path('add', views.add),
    # path('remove', views.remove),
    path('', views.index),
    # path('post/', views.post),


]
