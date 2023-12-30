# Project description

- This app is a parser for the site [jsonplaceholder](https://jsonplaceholder.typicode.com/) with Django functionality.
The user can parsering, collect via id from 1 to 10 the data about other users of the site 
and see it in this application.
---
# Instructions for configuring and launching the project

**1.** Clone the repository:

    git clone https://github.com/bezkrovnyyav/Django_parser.git
   
**2.** Create a virtual environment and activate it in Windows:

    cd Django_parser
    python -m venv env
    env\Scripts\activate

**3.** Install dependencies:

    pip install -r requirements.txt

**4.** Make migrations:

    python manage.py makemigrations

**5.** Create a database:

    python manage.py migrate
	
**6.** You can also create default superuser
    with the name - admin and password - admin via command:

    python manage.py createcustomadmin

**7.** Start the app:

    python manage.py runserver
	
