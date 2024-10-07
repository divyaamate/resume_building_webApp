"""
URL configuration for resumeproject project.

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
from django.urls import path
from resumeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('register/',views.register),
    path('save_user/',views.save_user),
    path('dologin/',views.dologin),
    path('home/',views.home),
    path('profile/',views.profile),
    path('resumetemplate/',views.resumetemplate),
    path('resume1/',views.resume1),
    
    path('save_contactDetails/',views.save_contactDetails),
    path('save_education/',views.save_education),
    path('save_objective/',views.save_objective),
    path('save_project/',views.save_project),
    path('save_course/',views.save_course)
    # path('dropdown/', views.dropdown),
    
]
