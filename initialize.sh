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
POSTGRES_USER=$username
POSTGRES_PASSWORD=$password
POSTGRES_DB=$database

export POSTGRES_USER
export POSTGRES_PASSWORD
export POSTGRES_DB

sudo -u postgres psql --command="CREATE DATABASE $POSTGRES_DB;"
sudo -u postgres psql --command="CREATE USER $POSTGRES_USER WITH ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';"
sudo -u postgres psql --command="ALTER ROLE $POSTGRES_USER SET client_encoding TO 'utf8';"
sudo -u postgres psql --command="ALTER ROLE $POSTGRES_USER SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql --command="ALTER ROLE $POSTGRES_USER SET timezone TO 'UTC';"
sudo -u postgres psql --command="GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;"
echo POSTGRES_USER=$POSTGRES_USER > .env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .env
echo POSTGRES_DB=$POSTGRES_DB >> .env
