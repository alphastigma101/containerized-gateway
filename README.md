## Table of Contents

1. [Introduction](#problem-statement)
3. [System Requirements](#system-requirements)
3. [Install Docker (Linux)](#linux-install)
    - [Running Our Product In Linux](#linux-environment)
4. [Install Docker (Windows)](#windows-install)
    - [Running Our Product In Windows](#windows-environment)
5. [Install Docker (MacOs)](#macos-install)
    - [Running Our Product in MacOs](#macos-environment)
9. [Troubleshooting](#troubleshooting)
    - [Common Issues](#common-issues)
    - [Logs and Diagnostic Data](#logs-and-diagnostic-data)
10. [Additional Resources](#additional-resources)



#### Problem Statement

Many organizations collect data that can be useful to researchers and data scientists outside (and within) the organization. An organization may be storing their data locally but have no way for others to access it or may not even have a good storage solution at all.

### Project Goals

- **A**)  Create a Python application to give to an organization that lets the admin users of the organization either create a new, robust Postgres database and initialize it with their own data or connect the application to an already-existing database owned by the organization.

- **B**)    Create a user-friendly GUI with Django that enables users to securely add and query data to/from the database.

- **C**)    Create a REST API that allows seamless querying and interaction with the application’s database from other machines over the internet, ensuring secure, scalable, and efficient data sharing and retrieval.

- **D**)    Containerize the application with Docker to allow for easy deployment by the organization with the help of Kubernetes for deployment.


#### System Requirements

* **RAM**: At least 4GB of RAM.
* **CPU**: Any modern 64-bit processor (typically Intel or AMD).
* **Storage**: At least 20GB of free disk space to accommodate images, containers, and volumes.
* **Operating System**: Windows 10 or macOS 10.14 and any Linux distributions that support docker

#### Linux-Install
* To offically use our product you need to install docker on your system. If you're a **linux user**, you can use these commands to install docker:
```
 sudo apt-get install docker-cli 
```
#### Windows-Install
* If you are a Windows user, you can simply follow this doc: *https://docs.docker.com/desktop/install/windows-install/*


