# Recipe Maker Food Application
## Members
- Ye Yuan (@liveyuanye)
- Welson Kuang (@welsonk)

## Presentation link
https://drive.google.com/file/d/1l1O0YOnh5gcKZhtLyMEmrfxkf8ucMJKR/view?usp=drive_link

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Implementation of Functional Requirements](#implementation-of-functional-requirements)

## General Info
This application is a recipe database website. Authorized users can create, delete, and view recipes. The recipe database can be seen by any authorized users.
	
## Technologies
This project is created with:
* Flask==3.0.3
* Flask-SQLAlchemy==3.1.1
* Flask-WTF==1.2.1
* Flask-Login==0.6.3
* SQLAlchemy==2.0.40
* WTForms==3.2.1
* Jinja2==3.1.6
* Werkzeug==3.1.3
* itsdangerous==2.2.0
* click==8.1.8

	
## Setup
Clone the repository:
```
$ git clone https://github.com/liveyuanye/Milestone-2-Initial-Implementation.git
```
Navigate into the project directory:
```
$ cd Milestone-2-Initial-Implementation
```
To run this project, create a virtual evironment:
```
$ python3 -m venv venv
```
Activate the virtual environment macOS / Linux:
```
$ source venv/bin/activate
```
Activate the virtual environment Windows (cmd / PowerShell):
```
$ .\venv\Scripts\activate
```

Install the necessary libraries from [Technologies](#technologies) using:
```
$ pip install -r requirements.txt
```
Then run the application using:
```
$ flask run
```

## Implementation of Functional Requirements
### Welson
1. A Sign Up form must be implemented to collect a user's username, password, and email.
2. A Log In form will allow users to login using their email and password.
3. The system must provide the the user the option to Log Out.
### Ye
4. A New Recipe form prompts the user for a recipe title, description, ingredients, and instructions.
5. A Delete Recipe option must be implemented to allow users to permanently remove their recipes from the database.
6. A View Recipe feature must enable users to view all details of a selected recipe, including title, description, ingredients, and instructions.
7. A View All Recipes feature must allow users to browse all recipes available in the database.

---
