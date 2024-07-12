from django import template
from app.db import Create, Query, Delete, Update

register = template.Library()

class Tags:
    """
    This class provides static methods for creating, querying, deleting,
    and updating data, wrapping around the corresponding functions in app.db.
    """
    
    @staticmethod
    def create_data():
        """
        Wrapper method for the Create function from app.db.

        Returns:
            The result of the Create function.
        """
        return Create()

    @staticmethod
    def query_data():
        """
        Wrapper method for the Query function from app.db.

        Returns:
            The result of the Query function.
        """
        return Query()
    
    @staticmethod
    def delete_data():
        """
        Wrapper method for the Delete function from app.db.

        Returns:
            The result of the Delete function.
        """
        return Delete()
    
    @staticmethod
    def update_data():
        """
        Wrapper method for the Update function from app.db.

        Returns:
            The result of the Update function.
        """
        return Update()

class Filters:
    # TODO:
        # This needs to be implemented 
    pass


# Register your template tag methods

#register.simple_tag(Tags.query_date, name="query_data")
#register.simple_tag(Tags.update_data, name="update_data")
#register.simple_tag(Tags.delete_data, name="delete_data")

