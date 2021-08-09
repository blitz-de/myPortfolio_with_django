"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import jobs.views
from django.conf import settings
from django.conf.urls.static import static

import jobs.views

urlpatterns = [
    path('', jobs.views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    # path('home', jobs.views.home, name='home'),
    path('jobs/<int:job_id>', jobs.views.detail, name='detail'),
    path('resume', jobs.views.resume, name='resume'),
    path('portfolio/', jobs.views.portfolio, name='portfolio'),
    path('aboutme/', jobs.views.aboutme, name='aboutme'),
    path('certifications/', jobs.views.certifications, name='certifications'),
    path('contact/', jobs.views.contact, name='contact'),
    # if someone goes to jobs/ and provide an int, then we want to save that int into a variable called job_id
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('i18n/', include('django.conf.urls.i18n')),
#     path('admin/', admin.site.urls),
#     path('', jobs.views.homepage, name='homepage'),
#     # path('home', jobs.views.home, name='home'),
#     path('jobs/<int:job_id>', jobs.views.detail, name='detail'),
#     path('resume', jobs.views.resume, name='resume'),
#     path('portfolio/', jobs.views.portfolio, name='portfolio'),
#     path('aboutme/', jobs.views.aboutme, name='aboutme'),
#     path('certifications/', jobs.views.certifications, name='certifications'),
#     path('contact/', jobs.views.contact, name='contact'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)