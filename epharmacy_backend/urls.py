"""
URL configuration for epharmacy_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import re
from django.contrib import admin
from django.urls import path, re_path as url, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autho/', include('autho.urls')),
    path('pharmacy/', include('pharmacy.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('invoice/', include('invoice.urls')),
    path('features/', include('features.urls')),
    path('home/', include('home.urls')),
]

static_media_url = [
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve, kwargs={'document_root': settings.MEDIA_ROOT}),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, kwargs={'document_root': settings.STATIC_ROOT})
]

urlpatterns += static_media_url
