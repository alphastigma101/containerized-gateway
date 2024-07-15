
def create_table(table_name, table_description):
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
    with open("models.py", 'a') as f:
        f.write(template)


create_table("User rePorts", "So funny story, I already typed all of this code a couple of days ago, but I mistakenly deleted the entire repo thinking that it was a backup. Fun fact: it was not. So anyways, I am just going to keep typing this absolute garbage of a text chunk in order to fill up space in the void that the galazy has conquered from the very beginning of all of time despite the fact that rice had nothing to do with it. Anyways, what have you done today? I know that I, personally, have studied enough Japanese to last a lifetime. And CUT.")
