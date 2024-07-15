# This script takes the variables in the .env file and exports them to the environment for Docker Compose to use.

export $(grep -v '^#' .env | xargs)
