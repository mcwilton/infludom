from . import views

from django.urls import path

# from main.views import HomePageView
#
urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    # path('add', views.add),
    # path('remove', views.remove),
    path('', views.index),
    # path('post/', views.post),

]
