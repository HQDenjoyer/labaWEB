"""
URL configuration for laba2WEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static, settings
from django.views.generic import TemplateView

from web.views import tr_handler403,tr_handler404,tr_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='web/home.html'), name='home'),
    path('users/', include('users.urls')),
    path('news/', include('news.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler403 = tr_handler403
handler500 = tr_handler500
handler404 = tr_handler404