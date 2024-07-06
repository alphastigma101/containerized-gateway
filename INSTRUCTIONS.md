### How to run
1. Clone the branch    
```
$ git clone -b django_initialization --single-branch git@github.com:alphastigma101/containerized-gateway.git
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
$ pip install -r requirements.txt
```
5. Initialize the PostgreSQL database and a new user     
```
$ bash initialize.sh -u <new_username> -p <new_password> -d <new_database_name>
```
6. Enter the project directory     
```
$ cd app
```
7. Start the Django server     
```
$ python3 manage.py runserver
```
8. View the webpage at [http://127.0.0.1:8000/gateway/home](http://127.0.0.1:8000/gateway/home)      
