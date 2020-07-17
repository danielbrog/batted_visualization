# Visualize batting data

#### To build the project, follow the steps below

##### Set up Virtual Environment
set up a virtual environment with Python running at version 3.7 and django

##### Run the commands Below to build the database
python3.7 manage.py makemigrations  
python3.7 manage.py makemigrations visualization_app  
python3.7 manage.py migrate  
python3.7 import_data.py  

##### Run the command below to start the server
python3.7 manage.py runserver  
Then open a web browser and navigate to localhost:8000
