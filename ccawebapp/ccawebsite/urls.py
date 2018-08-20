"""ccawebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from cca import views
from django.contrib import admin
#from django.contrib.auth import views.login
from django.urls import path,include
from django.views.generic.base import TemplateView
urlpatterns = [
    path('',views.home,name='home'),
    path('wdct/', TemplateView.as_view(template_name='wdct.html'), name='wdct'),
    path('core/', TemplateView.as_view(template_name='core.html'), name='core'),
    path('ecell/', TemplateView.as_view(template_name='ecell.html'), name='ecell'),
    path('robo/', TemplateView.as_view(template_name='robo.html'), name='robo'),
    path('r&d/', TemplateView.as_view(template_name='r&d.html'), name='r&d'),
	path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
