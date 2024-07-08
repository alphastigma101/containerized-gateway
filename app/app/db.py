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
from django.db import IntegrityError, transaction
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
    breakpoint()
    # Need to check and see if the user has a existing database 
    # If not, call in Data which will be a entity inside the database table 
    #create_parent()
    #try:
       # with transaction.atomic():
            #generate_relationships()
    #except IntegrityError:
        #handle_exception()

    #add_children()

