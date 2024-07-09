"""
Disabling autocommit ensures Django uses regular database transaction behavior, allowing rollback capabilities in case of errors during transactions.

The `atomic` function and its decorator are crucial for managing transaction blocks effectively. Key points about using `atomic`:
    1. Nesting is supported, enabling rollback of nested transactions if exceptions occur.
    2. Database changes are committed only if the decorated function completes without errors.

This approach complements the `SERIALIZABLE` isolation level configured in `settings.py`. This setting prevents anomalies during database serialization, ensuring application stability.

For more information:
    - `atomic` function: https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic
    - PostgreSQL Serialization: https://www.postgresql.org/docs/current/transaction-iso.html
"""
import datetime
from django.db import IntegrityError, DatabaseError, transaction, connection
from django import template
from gateway.models import Data, Report, System


"""
    Alternatives to avoid using the Jinja2 template engine as the backend for calling a function inside an HTML file.

    Options:
    1. Convert the function into a dictionary format and invoke it directly within the template engine.
    2. Implement custom template tags while abstracting the logic to avoid creating additional folder structures. Utilize decorators directly on the function.

    To remove custom template tags:
        - Remove the template library import and associated decorators.

    For further details, refer to the Django documentation on custom template tags:
        - https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/
"""
register = template.Library()


@transaction.atomic(using=None, savepoint=True, durable=True)
def Update(request):
    '''
        This function is embeded into the update_data.html and will update the database if the transaction is successful
        Otherwise, it will rollback to its origonal state
    '''
    create_parent()
    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()

    add_children()

@transaction.atomic(using=None, savepoint=True, durable=True)
def Insert(request):
    '''
        This function is embeded into the insert_data.html and will insert data into the database if the transaction is successful
        Otherwise, it will rollback to its origonal state
    '''
    create_parent()
    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()

    add_children()

@transaction.atomic(using=None, savepoint=True, durable=True)
def Delete(request):
    '''
        This function is embeded into the delete_data.html and will remove the entities if the transaction is successful
        Otherwise, it will rollback to its origonal state
    '''
    create_parent()
    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()

    add_children()


@transaction.atomic(using=None, savepoint=True, durable=True)
def Query(request):
    '''
        This function is embeded into the query_data.html and will return the requested query from the database if the transaction is successful
        Otherwise, report the error
        Here is a section where you can query your database:
             - https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.render
            https://docs.djangoproject.com/en/5.0/topics/db/transactions/
             - https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic
            https://docs.djangoproject.com/en/5.0/topics/db/models/
             - https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.JSONField
            https://docs.djangoproject.com/en/5.0/ref/databases/
            https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#howto-writing-custom-template-tags
        There is a way to query the database table entities it was in the user manual and their example was using a class called Fruit 
    '''
    create_parent()
    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()

    add_children()

@transaction.atomic(using=None, savepoint=True, durable=True)
def Create(request):
    '''
        This function is embeded into nothing. It will be called inside manage.py. It will crash if a database already exists 
    '''
    try:
        # Ensure the Data table exists
        from django.core.management import call_command
        # Run migrations to ensure the database schema is up to date
        call_command('makemigrations')            
        call_command('migrate')
        # Check if the Data table exists
        table_exists = 'data' in connection.introspection.table_names()
        if not table_exists:
            with connection.schema_editor() as schema_editor:
                schema_editor.create_model(Data)
            # Otherwise, create a couple of entities for it
            Data.objects.create(name='Entry 1')
            Data.objects.create(name='Entry 2')
            Data.objects.create(name='Entry 3')
            Data.objects.create(name='Entry 4')
            print("Finished creating Database Table")
            return
        else:
            print("Database already exists!")
            return
    except DatabaseError as e:
        # Handle any potential database errors
        # TODO: 
                # Either implement some logging here or just return nothing
        print(e)



