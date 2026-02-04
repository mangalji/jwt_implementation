<!-- step 1:
    

    git clone https://github.com/mangalji/jwt_implementation.git

step 2:
    create a virtual environment:
    In Linux: python3 -m venv <your venv name>
    then activate it by : 

        source <your venv name>/bin/activate

step 3: install the dependencies

    pip install requirements.txt

step 4: run the project

    python3 manage.py runserver
 -->
# JWT Implementation Project

This project demonstrates JWT (JSON Web Token) implementation using Django.

## Prerequisites

- Python 3.x
- Git

## Setup Instructions

- change the database settings with your credentials and details in settings.py 

### Step 1: Clone the Repository

```bash

git clone https://github.com/mangalji/jwt_implementation.git

cd jwt_implementation

```
### Step 2: Create and Activate a Virtual Environment
```

python3 -m venv <your_venv_name>

source <your_venv_name>/bin/activate

```
### Step 3: Install Dependencies
```
pip install -r requirements.txt

```
### Step 4: Run the Project
```
python3 manage.py runserver

```
### Step 5: Access the Application
```
http://127.0.0.1:8000/advocates
```
for generate the tokens: 
```
http://127.0.0.1:8000/token
```
copy the access token and open the postman and search the authorization and choose bearer and put that access token. Then again search the url with get method on postman:

```
http://127.0.0.1:8000/advocates
```
for get the data in detail:
```
http://127.0.0.1:8000/advocates/<username>
```