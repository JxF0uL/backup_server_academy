"""
URL configuration for AOEP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from Core.views import Homepage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #accounts_urls
    path('accounts/', include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name="homepage"),
    path('core/', include("Core.urls")),
    path('dashboard/', include("Dashboard.urls")),
]

# Adicione esta linha no final do arquivo, fora da lista urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Se você também estiver usando arquivos de mídia, adicione esta linha
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
