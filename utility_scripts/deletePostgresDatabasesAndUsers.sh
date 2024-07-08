#!/bin/bash

# Description:
# This script will delete any non-default (user-created) Postgres databases and users for a clean slate.
# Everytime you run the initialize.sh script, it makes a new database and user, so they build up after a while.

temp_file="to_delete.txt"

# Fetch all user-made Postgres databases to delete
sudo -u postgres psql --command="SELECT datname FROM pg_database WHERE datistemplate='False';" > $temp_file

delete_database() {
    echo "Deleting Database: $1" && sudo -u postgres psql --command="DROP DATABASE $1;"    
}

# Start reading from the third line of the database list
sed -n '3,$p' $temp_file | while read line
do
    # Skip lines with parentheses or that are empty/blank
    if [[ $line != *"("* ]] && [[ $line != *")"* ]] && [[ ! -z $line ]] && [[ $line != "postgres" ]]; then
        delete_database "$line"
    fi
done


# Fetch all Postgres users to delete
sudo -u postgres psql --command="SELECT usename FROM pg_catalog.pg_user WHERE usesuper='False'" > $temp_file

delete_user() {
    echo "Deleting User: $1" && sudo -u postgres psql --command="DROP USER $1;"    
}

# Start reading from the third line of the user list
sed -n '3,$p' $temp_file | while read line
do
    # Skip lines with parentheses or that are empty/blank
    if [[ $line != *"("* ]] && [[ $line != *")"* ]] && [[ ! -z $line ]] && [[ $line != "postgres" ]]; then
        delete_user "$line"
    fi
done

rm $temp_file
