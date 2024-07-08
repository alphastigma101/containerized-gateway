#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# TODO:
# Worry about implementing this later.. July 8th, 2024
#from psycopg import connect, ClientCursor # Binds cursor on front end which allows to query the data from the client to the server side: https://www.psycopg.org/psycopg3/docs/advanced/cursors.html#client-side-binding-cursors



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

"""
This script launches the application and ensures necessary databases are created if they do not exist.

Before launching the application, this script checks for the existence of required databases. If they
are not found, it creates them. Otherwise, it proceeds to launch the application normally.

For more information on database configuration in Django, refer to:
https://docs.djangoproject.com/en/5.0/ref/databases/
"""
if __name__ == '__main__':
    # Things I want to probably use:
        # https://docs.djangoproject.com/en/5.0/ref/databases/#server-side-cursors
        # https://docs.djangoproject.com/en/5.0/ref/databases/#manually-specifying-values-of-auto-incrementing-primary-keys

    #User.objects.create(username="alice", pk=1)

  
    # TODO:
        # This is where the database should be created if it does not exists otherwise initialize it 
    main()
