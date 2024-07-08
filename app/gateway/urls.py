from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("login", views.login, name="login"),
    path("update_data", views.update_data, name="update_data"),
    path("delete_data", views.delete_data, name="delete_data"),
    path("query_data", views.query_data, name="query_data")
]
