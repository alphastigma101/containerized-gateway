"""
URL configuration for app project.

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
from django.urls import include, path
from gateway import views  # Import views module from current directory

urlpatterns = [
    path("home", views.home, name="home"),
    path("update_data", views.update_data, name="update_data"),
    path("upload_data", views.upload_data, name="upload_data"),
    path("delete_data", views.delete_data, name="delete_data"),
    path("query_data", views.query_data, name="query_data"),
    path("bug_report", views.bug_report, name="bug_report"),
    path("about_us", views.about_us, name="about_us"),
    path("view_tables", views.view_tables, name="view_tables"),
    path("create_table", views.create_table, name="create_table"),
] 

