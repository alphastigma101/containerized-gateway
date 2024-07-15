# This file contains all of the helper functions for interacting with
# the PostgreSQL database

# For files writes, you must first navigate into the 'gateway' directory.


def create_table_helper(table_name, table_description):
    '''
    This function will create a new Django Model in models.py and migrate the new changes.
    Returns the formatted name of the model created.

    params:
    table_name  -> the name of the model to make
    table_description   -> a description of the contents of the table
    '''
    # Format the table name
    name = table_name.lower().title().replace(' ', '_')

    # Format the table description
    description = ""
    chars_per_line = 75
    curr_char = 0

    for c in table_description:
        curr_char += 1
        
        if curr_char >= 80 and c == ' ':
            description += '\n'
            curr_char = 0
            continue

        description += c

    # Insert the given info into the database class template
    template = f"""
class {name}(models.Model):
    \'\'\'
    {description}
    \'\'\'
    issue = models.CharField(max_length=30)
    date = models.CharField(max_length=8)  # Must be in valid date format
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """

    # Add the new model to models.py
    with open("gateway/models.py", 'a') as f:
        f.write(template)

    # Return the formatted name of the model
    return name


