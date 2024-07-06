#### Problem Statement

Many organizations collect data that can be useful to researchers and data scientists outside (and within) the organization. An organization may be storing their data locally but have no way for others to access it or may not even have a good storage solution at all.

### Project Goals

**A.**  Create a Python application to give to an organization that lets the admin users of the organization either create a new, robust Postgres database and initialize it with their own data or connect the application to an already-existing database owned by the organization.

**B.**    Create a user-friendly GUI with Django that enables users to securely add and query data to/from the database.

**C.**    Create a REST API that allows seamless querying and interaction with the application’s database from other machines over the internet, ensuring secure, scalable, and efficient data sharing and retrieval.

**D.**    Containerize the application with Docker to allow for easy deployment by the organization with the help of Kubernetes for deployment.

