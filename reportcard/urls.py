"""
URL configuration for reportcard project.

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
from django.conf import settings
from django.conf.urls.static import static

from reports.views import *

urlpatterns = [
    
    path('report/', include('reports.urls')),
    path('students/', get_students, name="get_students"),
    path('generate_otp/<student_id>/', generate_and_send_otp, name="generate_otp"),
    path('verify_otp/', verify_otp, name="verify_otp"),
    path('resend_otp/', resend_otp, name="resend_otp"),
    path('see_marks/<student_id>/', see_marks, name="see_marks"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root = settings.MEDIA_ROOT)
