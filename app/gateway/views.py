from django.shortcuts import render
from django.http import HttpResponse
from app.poll_extras import Tags

from django.apps import apps
from django.db import connection
import os
import django

from .forms import CreateTableForm
from .database_helper_functions import create_table_helper

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


def view_tables(request):
    if request.method == "POST":
        # Fetch all model names and omit Django-made ones
        model_names = [m._meta.db_table for c in apps.get_app_configs() for m in c.get_models()]
        django_models = ['django_admin_log', 'auth_permission', 'auth_group', 'auth_user', 'django_content_type', 'django_session']
        
        user_models = []
        for name1 in model_names:
            if name1 not in django_models:
                user_models.append(name1)

        return render(request, 'view_tables.html', {'response':'Custom Tables', 'models':user_models})

    return render(request, 'view_tables.html', {})


def create_table(request):
    empty_form = CreateTableForm()
    
    # When the user hits the "submit" button
    if request.method == 'POST':
        form = CreateTableForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data # Submitted-form contents
            name = form_data['name']
            desc = form_data['description']

            # Create the table
            formatted_name = create_table_helper(name, desc)
            
            return render(request, 'create_table.html', {'form': empty_form, 'message': f'Successfully created a new table: {formatted_name}'})
        else:
            return render(request, 'create_table.html', {'form': empty_form, 'message':""})

    # Render the default create table page
    return render(request, 'create_table.html', {'form': empty_form, 'message':""})
