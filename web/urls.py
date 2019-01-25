"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from schooldetails.views import Schooldetails_list,School_details,School_core,Specialty_details,inquiry,inquiry_core

urlpatterns = (
    path('<int:list_pk>', Schooldetails_list, name='schoollist'),
    path('admin/', admin.site.urls),
    path('', Schooldetails_list, name='home', kwargs={'list_pk': '1'}),
    path('schooldetail/<int:school_pk>', School_details, name='schooldetail'),
    path('schoolcore/', School_core, name='schoolcore'),
    path('specialtydetail/', Specialty_details, name='specialtycore'),
    path('inquiry/', inquiry, name='inquiry'),
    path('inquiry_core/', inquiry_core, name='inquiry_core'),
)
