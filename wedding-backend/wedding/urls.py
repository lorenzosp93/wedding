"""wedding_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'Priscilla and Lorenzo'
admin.site.site_title = 'Priscilla and Lorenzo'

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/health/', include('health_check.urls')),
    path('api/api-auth/', include(
        'rest_framework.urls', namespace='rest_framework',
    )),
    path('api/guestbook/', include('guestbook.urls')),
    path('api/inbox/', include('inbox.urls')),
    path('api/shared/', include('shared.urls')),
    path('api/', include('info.urls')),
    path('api/user/', include('profile.urls')),
    path('api/', include('drfpasswordless.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
