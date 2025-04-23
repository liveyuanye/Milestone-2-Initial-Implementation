# Recipe Maker Food Application
## Members
- Ye Yuan (@liveyuanye)
- Welson Kuang (@welsonk)

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Implementation of Functional Requirements](#implementation-of-functional-requirements)

## General Info
This application is a recipe database website. Authorized users can create, delete, and view recipes. The recipe database can be seen by any authorized users.
	
## Technologies
This project is created with:
* Flask version: 2.0.1
* Flask-SQLAlchemy version: 2.5.1
* Flask-WTF version: 0.15.1
* Flask-Login version: 0.5.0
	
## Setup
To run this project, create a virtual evironment:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
Install the necessary libraries from [Technologies](#technologies) using:
```
$ pip3 install <library>
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
