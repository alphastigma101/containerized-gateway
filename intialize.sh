#!/bin/bash

# Initialize our own variables
username=""
password=""
database=""

# Parse the command line options
while getopts ":u:p:d:" opt; do
  case ${opt} in
    u)
      username="$OPTARG"
      ;;
    p)
      password="$OPTARG"
      ;;
    d)
      database="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# Check if flags are set
if [ -z "$username" ] || [ -z "$password" ] || [ -z "$database" ]; then
    echo "All flags -u (username), -p (password), and -d (database) must be set."
    exit 1
fi

# Make the database and credentials
#sudo apt-get install postgresql postgresql-contrib
#sudo apt-get install libpq-dev python3-dev
POSTGRES_USERNAME=$username
POSTGRES_PASSWORD=$password
POSTGRES_DATABASE=$database
echo "CREATE DATABASE $POSTGRES_DATABASE;" > make_user.txt
echo "CREATE USER $POSTGRES_USERNAME WITH ENCRYPTED PASSWORD '$POSTGRES_PASSWORD'" >> make_user.txt
#sudo chmod og+rX /home/user
#sudo -u postgres psql --file="make_user.txt"
#rm make_user.txt
echo POSTGRES_USERNAME=$POSTGRES_USERNAME >> .env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .env
echo POSTGRES_DATABASE=$POSTGRES_DATABASE >> .env
