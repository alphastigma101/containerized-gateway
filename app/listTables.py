import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

# Initialize Django
django.setup()

from django.apps import apps
from django.db import connection

# Get all table names
table_names = connection.introspection.table_names()

# Get all model names
model_names = [m._meta.db_table for c in apps.get_app_configs() for m in c.get_models()]

print("Table names: ", table_names)
print("Model names: ", model_names)
