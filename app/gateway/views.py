from django.shortcuts import render
from django.http import HttpResponse
from app.poll_extras import Tags


def home(request):
    Tags.create_data
    return render(request, "home.html")

def update_data(request):
    return render(request, "update_data.html")

def delete_data(request):
    return render(request, "delete_data.html")

def query_data(request):
    return render(request, "query_data.html")

def about_us(request):
    return render(request, 'about_us.html')

def bug_report(request):
    return render(request, 'bug_report.html')

def upload_data(request):
    return render(request, 'upload_data.html')



