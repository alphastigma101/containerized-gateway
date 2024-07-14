import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

# Initialize Django
django.setup()
