## Table of Contents

1. [Introduction](#problem-statement)

2. [Why Use Our Product](#why-use-our-product)

2. [System Requirements](#system-requirements)

3. [Running Our Product (Without Docker)](#running-our-product-without-docker)

4. [Running Our Product (With Docker)](#running-our-product-with-docker)
    - [Install Docker (Linux)](#linux-install)
    - [Running Our Product (Linux)](#linux-environment)
5. [Install Docker (Windows)](#windows-install)
    - [Running Our Product (Windows)](#windows-environment)
6. [Install Docker (MacOs)](#macos-install)
    - [Running Our Product (MacOs)](#macos-environment)

7. [Troubleshooting](#troubleshooting)
    - [Common Issues](#common-issues)
    - [Logs and Diagnostic Data](#logs-and-diagnostic-data)
8. [Additional Resources](#additional-resources)
    -  [Docker Sources](#docker-sources)




#### Problem Statement

Many organizations collect data that can be useful to researchers and data scientists outside (and within) the organization. An organization may be storing their data locally but have no way for others to access it or may not even have a good storage solution at all.

### Project Goals

- **A**)  Create a Python application to give to an organization that lets the admin users of the organization either create a new, robust Postgres database and initialize it with their own data or connect the application to an already-existing database owned by the organization.

- **B**)    Create a user-friendly GUI with Django that enables users to securely add and query data to/from the database.

- **C**)    Create a REST API that allows seamless querying and interaction with the application’s database from other machines over the internet, ensuring secure, scalable, and efficient data sharing and retrieval.

- **D**)    Containerize the application with Docker to allow for easy deployment by the organization with the help of Kubernetes for deployment.

#### Why Use Our Product
* Our product provides stability and transfers data securely over the internet for free unlike most products 
* It is easy to use and is easy to navigate and if there is a bug, you can report bugs! 

#### System Requirements

* **RAM**: At least 4GB of RAM.
* **CPU**: Any modern 64-bit processor (typically Intel or AMD).
* **Storage**: At least 20GB of free disk space to accommodate images, containers, and volumes.
* **Operating System**: Windows 10 or macOS 10.14 and any Linux distributions that support docker

### General Setup Instructions
1. Clone the branch    
```
$ git clone git@github.com:alphastigma101/containerized-gateway.git
```
2. Navigate into the cloned repo      
```
$ cd containerized_gateway
```
3. Make and activate a virtual environment     
```
$ python3 -m venv env
```
```
$ source env/bin/activate
```
4. Install the requirements     
```
$ pip install -r app/requirements.txt
```
5. Initialize the PostgreSQL database and a new user     
```
$ source intialize.sh -u <new_username> -p <new_password> -d <new_database_name>
```
6. Enter the project directory     
```
$ cd app
```

#### Running The App Without Docker
1. Follow the "General Setup Instructions" above
2. Start the Django server     
```
$ python3 manage.py runserver
```
3. View the webpage at [http://127.0.0.1:8000/gateway/home](http://127.0.0.1:8000/gateway/home)  

#### Running The App With Docker
1. Follow the "General Setup Instructions" above
2. Install Docker
3. Start the web app and database containers
```
$ docker compose up -d --build
```
> OPTIONAL: test database connection by running `$ docker-compose exec web python3 manage.py migrate`     
> Also, run PostgreSQL commands to interact with the database container with `$ docker-compose exec -it db psql -U <POSTGRES_USERNAME> -d <POSTGRES_DB_NAME> -c`
4. View the webpage at [http://127.0.0.1:8000/gateway/home](http://127.0.0.1:8000/gateway/home)  
> To stop the containers, run `$ docker compose down --volumes`     
> To debug the app, run `docker compose up -build`

#### Linux-Install
* To offically use our product you need to install docker on your system. If you're a **linux user**, you can use these commands to install docker:
```
 sudo apt-get update 
 sudo apt-get install docker-cli  docker-compose-plugin 
```
* If ubuntu can't find docker-compose-plugin then you need to copy this code below and paste it into your terminal:

```

sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

* To start the container:
```
docker compose up -d --build

```
* Then in your browser, paste this into it: ``` http://localhost:8000/ ```
* To stop it: 
```
docker compose down --volumes

```

* To debug it:
```
docker compose up -build
```
* **Note For Debugging**: **you must use CTL+C to exit out**


#### Windows-Install
* If you are a Windows user, you can simply follow this doc: *https://docs.docker.com/desktop/install/windows-install/*



#### MacOs-Install
* **FMI**

#### Additinal Resources
* **FMI**

#### Docker Sources

* *https://docs.docker.com/guides/docker-concepts/running-containers/publishing-ports/*
* *https://docs.docker.com/guides/getting-started/build-and-push-first-image/*
* *https://docs.docker.com/reference/dockerfile/*
* *https://docs.docker.com/build/guide/intro/*
* *https://docs.docker.com/compose/intro/features-uses/*
* *https://docs.docker.com/engine/swarm/*
* *https://docs.docker.com/build/guide/multi-stage/*


