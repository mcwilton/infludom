"""infludom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import include, path
from rest_auth.views import LoginView
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
# from .main import views

# from rest_framework_swagger.views import get_swagger_view


# schema_view = get_swagger_view(title='Pastebin API')


router = routers.DefaultRouter()
# router.register(r'talent', views.TalentViewSet)
# router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('main.urls')),
    path('api_urls/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/register/', include('rest_registration.api.urls')), # final registration
    # path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('api/', include('core.urls', namespace='api')),
    # path('api/v1/', include(api_urlpatterns)),
    # # url(r'^$', schema_view)
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
 ]



