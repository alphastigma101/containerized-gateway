from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def update_data(request):
    return render(request, "update_data.html")

def delete_data(request):
    return render(request, "delete_data.html")

def query_data(request):
    return render(request, "query_data.html")



