"""nepathya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.discography import views as discography_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', discography_views.index, name="home"),
    url(r'^discography/', include('apps.discography.urls')),
    url(r'^news/', include('apps.news.urls')),
    url(r'^gallery/', include('apps.gallery.urls')),
    url(r'^video/', include('apps.video.urls')),
    url(r'^events/', include('apps.events.urls')),
    url(r'^feedbacks/', include('apps.feedback.urls')),
    url(r'fcm/', include('fcm.urls')),
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)